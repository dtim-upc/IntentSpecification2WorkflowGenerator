<script lang="ts">
    import Button from "@smui/button";
    import Paper, {Content, Subtitle, Title} from '@smui/paper';
    import {createEventDispatcher} from 'svelte';
    import CircularProgress from '@smui/circular-progress';
    import Accordion, {Content as AccContent, Header, Panel} from '@smui-extra/accordion';
    import List, {Item, Label, Meta} from '@smui/list';
    import Checkbox from '@smui/checkbox';
    import IconButton from '@smui/icon-button';
    import {removeLastPart, windowsStyleSort} from "./utils";

    const dispatch = createEventDispatcher();

    let plans: {
        [key: string]: any
    };

    let creating_plans = false;

    let keys;
    let groups: {
        [key: string]: string[]
    };
    let selectedGroups: {
        [key: string]: string[]
    };

    async function initialize() {
        let response = await fetch('http://localhost:5000/logical_plans');
        plans = await response.json();
        keys = Object.keys(plans);
        groups = {};

        for (let key of keys) {
            let group = removeLastPart(key);
            if (!groups.hasOwnProperty(group)) {
                groups[group] = [];
            }
            groups[group].push(key);
        }

        selectedGroups = JSON.parse(JSON.stringify(groups));
    }

    let initializing = initialize();

    function toggle_group(event: any, group_id: string) {
        event.stopPropagation();
        if (selectedGroups[group_id].length !== groups[group_id].length) {
            selectedGroups[group_id] = JSON.parse(JSON.stringify(groups[group_id]));
        } else {
            selectedGroups[group_id] = [];
        }
    }

    function viewLogicalPlan(plan_id: string) {
        let plan = plans[plan_id];
        dispatch('visualize_plan', {plan: plan, plan_id: plan_id});
    }

    async function run_planner() {
        creating_plans = true;
        let selected: string[] = [];
        for (let group_selected of Object.values(selectedGroups)) {
            selected = selected.concat(group_selected);
        }

        await fetch('http://localhost:5000/workflow_planner', {
            method: 'POST',
            body: JSON.stringify(selected),
            headers: {
                'Content-Type': 'application/json'
            }
        });

        dispatch('workflow_plans');
        creating_plans = false;
    }

</script>

<Paper variant="unelevated" class="flex-column">
    <Title>Workflow Planner</Title>
    <Subtitle>Select the Logical Plans to send to the Workflow Planner:</Subtitle>
    <Content class="flex-column">
        {#if creating_plans}
            <CircularProgress style="height: 32px; width: 32px;" indeterminate/>
        {:else}
            {#await initializing}
                <CircularProgress style="height: 32px; width: 32px;" indeterminate/>
            {:then _}
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
                                <List class="demo-list" checkList>
                                    {#each windowsStyleSort(groups[group_id]) as element}
                                        <div class="item-div">
                                            <Item>
                                                <div class="inner-item-div">
                                                    <Meta>
                                                        <Checkbox bind:group={selectedGroups[group_id]}
                                                                  value="{element}"/>
                                                    </Meta>
                                                    <Label>{element}</Label>
                                                </div>
                                                <Meta>
                                                    <IconButton class="material-icons"
                                                                on:click={() => viewLogicalPlan(element)}>visibility
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
            {/await}
        {/if}
    </Content>

</Paper>


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