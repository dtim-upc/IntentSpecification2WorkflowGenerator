<script>
    import Button from "@smui/button";
    import Paper, {Content, Subtitle, Title} from '@smui/paper';
    import AbstractPlanVisualizer from "./AbstractPlanVisualizer.svelte";
    import {createEventDispatcher} from 'svelte';
    import CircularProgress from '@smui/circular-progress';
    import Accordion, {Content as AccContent, Header, Panel} from '@smui-extra/accordion';
    import List, {Item, Label, Meta} from '@smui/list';
    import Checkbox from '@smui/checkbox';
    import IconButton from '@smui/icon-button';

    const dispatch = createEventDispatcher();

    function removeLastPart(inputString) {
        const parts = inputString.split(' ');

        if (parts.length > 1) {
            parts.pop(); // Remove the last part
            return parts.join(' ');
        } else {
            return inputString; // Return the original string if there's only one part
        }
    }

    function windowsStyleSort(strings) {
        return strings.slice().sort((a, b) => {
            return a.localeCompare(b, undefined, {numeric: true, sensitivity: 'base'});
        });
    }

    export let plans;

    let creating_plans = false;

    let keys = Object.keys(plans);
    let groups = {};

    for (let key of keys) {
        let group = removeLastPart(key);
        if (groups[group] === undefined) {
            groups[group] = [];
        }
        groups[group].push(key);
    }

    let selectedGroups = JSON.parse(JSON.stringify(groups));
    let changeEvents = {};

    let open = false;
    let view_plan = undefined;

    function toggle_group(event, group_id) {
        event.stopPropagation();
        if (selectedGroups[group_id].length !== groups[group_id].length) {
            selectedGroups[group_id] = JSON.parse(JSON.stringify(groups[group_id]));
        } else {
            selectedGroups[group_id] = [];
        }
    }

    function viewWorkflowPlan(plan_id) {
        view_plan = plans[plan_id];
        open = true;
    }

    function closeVisualization(event) {
        open = false;
        view_plan = undefined;
    }

    async function run_planner() {
        creating_plans = true;
        let selected = [];
        for (let group_selected of Object.values(selectedGroups)) {
            selected = selected.concat(group_selected);
        }

        const response = await fetch('http://localhost:5000/workflow_planner', {
            method: 'POST',
            body: JSON.stringify(selected),
            headers: {
                'Content-Type': 'application/json'
            }
        });

        let plans = await response.json();
        dispatch('workflow_plans', plans);
        creating_plans = false;
    }

</script>

<Paper variant="unelevated" class="flex-column">
    <Title>Logical Planner</Title>
    <Subtitle>Select the Abstract Plans to send to the Logical Planner:</Subtitle>
    <Content class="flex-column">
        {#if creating_plans}
            <CircularProgress style="height: 32px; width: 32px;" indeterminate/>
        {:else}
            <Accordion>
                {#each Object.keys(groups) as group_id}
                    <Panel>
                        <Header>
                            <div class="center">
                                {group_id} ({selectedGroups[group_id].length}/{groups[group_id].length})
                                <IconButton class="material-icons"
                                            on:click={(event) => toggle_group(event, group_id)}
                                >
                                    {#if selectedGroups[group_id].length === groups[group_id].length}
                                        check_box
                                    {:else if selectedGroups[group_id].length === 0}
                                        check_box_outline_blank
                                    {:else}
                                        indeterminate_check_box
                                    {/if}
                                </IconButton>
                            </div>
                        </Header>
                        <AccContent>
                            <List
                                    class="demo-list"
                                    checkList
                                    on:SMUIList:selectionChange={(event) => (changeEvents[group_id] = event)}
                            >
                                {#each windowsStyleSort(groups[group_id]) as element}
                                    <div class="item-div">
                                        <Item>
                                            <div class="inner-item-div">
                                                <Meta>
                                                    <Checkbox bind:group={selectedGroups[group_id]} value="{element}"/>
                                                </Meta>
                                                <Label>{element}</Label>
                                            </div>
                                            <Meta>
                                                <IconButton class="material-icons"
                                                            on:click={() => viewAbstractPlan(element)}>visibility
                                                </IconButton>
                                            </Meta>
                                        </Item>
                                    </div>
                                {/each}
                            </List>
                        </AccContent>
                    </Panel>
                {/each}
            </Accordion>

            Total of {Object.values(selectedGroups).reduce((a, b) => a + b.length, 0)} Logical Plans selected.

            <Button on:click={run_planner} variant="outlined">
                <Label>Run Workflow Planner</Label>
            </Button>
        {/if}
    </Content>

</Paper>

{#if open}
    <AbstractPlanVisualizer open={open} plan={view_plan} on:close={closeVisualization}></AbstractPlanVisualizer>
{/if}
<style>
    .inner-item-div {
        display: flex;
        justify-content: left;
        align-items: center;
    }

    .center {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

</style>