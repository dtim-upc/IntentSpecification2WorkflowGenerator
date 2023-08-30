<script lang="ts">
    import Textfield from "@smui/textfield";
    import Button, {Label} from '@smui/button';
    import CircularProgress from '@smui/circular-progress';
    import Autocomplete from '@smui-extra/autocomplete';
    import {createEventDispatcher} from 'svelte';
    import Paper, {Content, Title} from '@smui/paper';


    const dispatch = createEventDispatcher();

    let datasets: {[key: string]: string} = {};
    let problems: {[key: string]: string} = {};

    let intent_name = '';
    let dataset = '';
    let problem = '';

    let loading_datasets = true;
    let loading_problems = true;

    let creating_plans = false;

    fetch('http://localhost:5000/datasets').then(response => response.json()).then(data => {
        datasets = data;
        loading_datasets = false;
    })

    fetch('http://localhost:5000/problems').then(response => response.json()).then(data => {
        problems = data;
        loading_problems = false;
    })

    async function run_planner(): Promise<void> {
        let final_dataset = datasets[dataset];
        let final_problem = problems[problem];

        creating_plans = true;

        await fetch('http://localhost:5000/abstract_planner', {
            method: 'POST',
            body: JSON.stringify({
                'intent_name': intent_name,
                'dataset': final_dataset,
                'problem': final_problem
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        dispatch('abstract_plans');
        creating_plans = false;
    }
</script>

<Paper variant="unelevated" class="flex-column">
    <Title>Abstract Planner</Title>
    <Content class="flex-column">
        {#if loading_datasets || loading_problems || creating_plans}
            <CircularProgress style="height: 32px; width: 32px;" indeterminate/>
        {:else}
            <Textfield variant="outlined" bind:value={intent_name} label="Intent name"></Textfield>
            <Autocomplete
                    options={Object.keys(datasets)}
                    textfield$variant="outlined"
                    bind:value={dataset}
                    label="Dataset"
            />
            <Autocomplete
                    options={Object.keys(problems)}
                    textfield$variant="outlined"
                    bind:value={problem}
                    label="Problem"
            />

            <Button on:click={run_planner} variant="outlined">
                <Label>Run Abstract Planner</Label>
            </Button>
        {/if}
    </Content>
</Paper>