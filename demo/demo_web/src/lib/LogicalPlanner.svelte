<script>
    import List, {Item, Label, Meta} from '@smui/list';
    import Checkbox from '@smui/checkbox';
    import IconButton from '@smui/icon-button';
    import Button from "@smui/button";
    import Paper, {Content, Subtitle, Title} from '@smui/paper';
    import AbstractPlanVisualizer from "./AbstractPlanVisualizer.svelte";
    import {createEventDispatcher} from 'svelte';
    import CircularProgress from '@smui/circular-progress';

    const dispatch = createEventDispatcher();

    export let plans;

    let creating_plans = false;

    let keys = Object.keys(plans);
    let selected = Object.keys(plans || {});
    let changeEvent;

    let open = false;
    let view_plan = undefined;

    function viewAbstractPlan(plan_id) {
        view_plan = plans[plan_id];
        open = true;
    }

    function closeVisualization(event) {
        open = false;
        view_plan = undefined;
    }

    async function run_planner() {
        creating_plans = true;

        const response = await fetch('http://localhost:5000/logical_planner', {
            method: 'POST',
            body: JSON.stringify(selected),
            headers: {
                'Content-Type': 'application/json'
            }
        });

        let plans = await response.json();
        dispatch('logical_plans', plans);
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
            <List
                    class="demo-list"
                    checkList
                    on:SMUIList:selectionChange={(event) => (changeEvent = event)}
            >
                {#each keys as key}
                    <div class="item-div">
                        <Item>
                            <div class="inner-item-div">
                                <Meta>
                                    <Checkbox bind:group={selected} value="{key}"/>
                                </Meta>
                                <Label>{key.split('#').at(-1)}</Label>
                            </div>
                            <Meta>
                                <IconButton class="material-icons" on:click={() => viewAbstractPlan(key)}>visibility
                                </IconButton>
                            </Meta>
                        </Item>
                    </div>
                {/each}
            </List>

            <Button on:click={run_planner} variant="outlined">
                <Label>Run Logical Planner</Label>
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

</style>