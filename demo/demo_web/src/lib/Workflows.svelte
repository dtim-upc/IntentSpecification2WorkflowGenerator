<script lang="ts">
    import Button from "@smui/button";
    import Paper, {Content, Subtitle, Title} from '@smui/paper';
    import Accordion, {Content as AccContent, Header, Panel} from '@smui-extra/accordion';
    import List, {Item, Label, Meta} from '@smui/list';
    import IconButton from '@smui/icon-button';
    import CircularProgress from "@smui/circular-progress";
    import Tooltip, {Wrapper} from '@smui/tooltip';


    function removeLastPart(inputString: string) {
        const parts = inputString.split(' ');

        if (parts.length > 1) {
            parts.pop(); // Remove the last part
            return parts.join(' ');
        } else {
            return inputString; // Return the original string if there's only one part
        }
    }

    function windowsStyleSort(strings: string[]) {
        return strings.slice().sort((a, b) => {
            return a.localeCompare(b, undefined, {numeric: true, sensitivity: 'base'});
        });
    }

    let plans: string[];
    let groups: {
        [key: string]: string[]
    };

    async function initialize() {
        let response = await fetch('http://localhost:5000/workflow_plans');
        plans = await response.json();
        groups = {};

        for (let key of plans) {
            let group = removeLastPart(key);
            if (!groups.hasOwnProperty(group)) {
                groups[group] = [];
            }
            groups[group].push(key);
        }
    }

    let initializing = initialize();

    async function download_rdf(plan_id: string) {
        let element = document.createElement('a');
        element.setAttribute('href', 'http://localhost:5000/workflow_plans/rdf/' + plan_id);
        element.setAttribute('download', 'rdf_plans.zip');
        element.click();
    }

    async function download_all_rdf() {
        let element = document.createElement('a');
        element.setAttribute('href', 'http://localhost:5000/workflow_plans/rdf/all');
        element.setAttribute('download', 'rdf_plans.zip');
        element.click();
    }

    function download_knime(plan_id: string) {
        let element = document.createElement('a');
        element.setAttribute('href', 'http://localhost:5000/workflow_plans/knime/' + plan_id);
        element.setAttribute('download', 'rdf_plans.zip');
        element.click();
    }

    function download_all_knime() {
        let element = document.createElement('a');
        element.setAttribute('href', 'http://localhost:5000/workflow_plans/knime/all');
        element.setAttribute('download', 'rdf_plans.zip');
        element.click();
    }

</script>

<Paper variant="unelevated" class="flex-column">
    <Title>Final Workflows</Title>
    {#await initializing}
        <CircularProgress style="height: 32px; width: 32px;" indeterminate/>
    {:then _}
        <Subtitle>Select the Abstract Plans to send to the Logical Planner:</Subtitle>
        <Content class="flex-column">
            <Accordion>
                {#each Object.keys(groups) as group_id}
                    <Panel>
                        <Header>{group_id}</Header>
                        <AccContent>
                            <List class="demo-list">
                                {#each windowsStyleSort(groups[group_id]) as element}
                                    <div class="item-div">
                                        <Item>
                                            <div class="inner-item-div">
                                                <Label>{element}</Label>
                                            </div>
                                            <Meta>
                                                <Wrapper>
                                                    <IconButton class="material-icons"
                                                                on:click={() => download_rdf(element)}>share
                                                    </IconButton>
                                                    <Tooltip>Download RDF representation</Tooltip>
                                                </Wrapper>
                                                <Wrapper>
                                                    <IconButton class="material-icons"
                                                                on:click={() => download_knime(element)}>download
                                                    </IconButton>
                                                    <Tooltip>Download KNIME representation</Tooltip>
                                                </Wrapper>
                                            </Meta>
                                        </Item>
                                    </div>
                                {/each}
                            </List>
                        </AccContent>
                    </Panel>
                {/each}
            </Accordion>

            <div>
                <Button on:click={download_all_rdf} variant="outlined">
                    <Label>Download all RDF representations</Label>
                </Button>
                <Button on:click={download_all_knime} variant="outlined">
                    <Label>Download all KNIME representations</Label>
                </Button>
            </div>
        </Content>
    {/await}

</Paper>

<style>
    .inner-item-div {
        display: flex;
        justify-content: left;
        align-items: center;
    }
</style>