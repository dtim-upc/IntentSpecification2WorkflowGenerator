<script lang="ts">
    import Card from "@smui/card";
    import AbstractPlanner from "./lib/AbstractPlanner.svelte";
    import Tab, {Icon, Label} from '@smui/tab';
    import TabBar from '@smui/tab-bar';
    import LogicalPlanner from "./lib/LogicalPlanner.svelte";
    import WorkflowPlanner from "./lib/WorkflowPlanner.svelte";
    import Workflows from "./lib/Workflows.svelte";

    let tabs = [
        {
            icon: 'access_time',
            label: 'Abstract Planner',
        },
        {
            icon: 'near_me',
            label: 'Logical Planner',
        },
        {
            icon: 'favorite',
            label: 'Workflow Planner',
        },
        {
            icon: 'favorite',
            label: 'Workflows',
        },
    ];

    let active = tabs[0];


    let abstract_plans = {};
    let logical_plans = {};
    let workflow_plans = {};

    function abstract_planner_finished(event) {
        abstract_plans = event.detail;
        active = tabs[1];
    }

    function logical_planner_finished(event) {
        logical_plans = event.detail;
        active = tabs[2];
    }

    function workflow_planner_finished(event) {
        workflow_plans = event.detail;
        active = tabs[3];
    }
</script>

<main>
    <link
            rel="stylesheet"
            href="node_modules/svelte-material-ui/themes/svelte.css"
            media="(prefers-color-scheme: light)"
    />
    <!-- Hint where we get fonts from. -->
    <link rel="preconnect" href="https://fonts.googleapis.com"/>
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>

    <!-- Material Icons, Roboto, and Roboto Mono fonts -->
    <link
            href="https://fonts.googleapis.com/css2?family=Material+Icons&Roboto+Mono:ital@0;1&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap"
            rel="stylesheet"
    />

    <div class="center">
        <Card padded>
            <TabBar {tabs} let:tab bind:active>
                <Tab {tab}>
                    <Icon class="material-icons">{tab.icon}</Icon>
                    <Label>{tab.label}</Label>
                </Tab>
            </TabBar>
            <div class:hide={active.label !== 'Abstract Planner'}>
                <AbstractPlanner on:abstract_plans={abstract_planner_finished}></AbstractPlanner>
            </div>
            {#if active.label === 'Logical Planner'}
                <LogicalPlanner plans={abstract_plans} on:logical_plans={logical_planner_finished}></LogicalPlanner>
            {/if}
            {#if active.label === 'Workflow Planner'}
                <WorkflowPlanner plans={logical_plans} on:workflow_plans={workflow_planner_finished}></WorkflowPlanner>
            {/if}
            {#if active.label === 'Workflows'}
                <Workflows plans={workflow_plans}></Workflows>
            {/if}
        </Card>
    </div>

</main>

<style>
    .center {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 90vh;
    }

    .hide {
        display: none !important;
    }
</style>