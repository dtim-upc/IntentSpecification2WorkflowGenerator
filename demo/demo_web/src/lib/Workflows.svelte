<script>
    import Button from "@smui/button";
    import Paper, {Content, Subtitle, Title} from '@smui/paper';
    import Accordion, {Content as AccContent, Header, Panel} from '@smui-extra/accordion';
    import List, {Item, Label, Meta} from '@smui/list';
    import IconButton from '@smui/icon-button';


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

    let groups = {};

    for (let key of plans) {
        let group = removeLastPart(key);
        if (groups[group] === undefined) {
            groups[group] = [];
        }
        groups[group].push(key);
    }

    let selectedGroups = JSON.parse(JSON.stringify(groups));

    function toggle_group(event, group_id) {
        event.stopPropagation();
        if (selectedGroups[group_id].length !== groups[group_id].length) {
            selectedGroups[group_id] = JSON.parse(JSON.stringify(groups[group_id]));
        } else {
            selectedGroups[group_id] = [];
        }
    }

    async function download_rdf(plan_id) {
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

    function download_knime(plan_id) {
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
    <Title>Logical Planner</Title>
    <Subtitle>Select the Abstract Plans to send to the Logical Planner:</Subtitle>
    <Content class="flex-column">
        <Accordion>
            {#each Object.keys(groups) as group_id}
                <Panel>
                    <Header>
                        {group_id} ({selectedGroups[group_id].length}/{groups[group_id].length})
                    </Header>
                    <AccContent>
                        <List class="demo-list">
                            {#each windowsStyleSort(groups[group_id]) as element}
                                <div class="item-div">
                                    <Item>
                                        <div class="inner-item-div">
                                            <Label>{element}</Label>
                                        </div>
                                        <Meta>
                                            <IconButton class="material-icons"
                                                        on:click={() => download_rdf(element)}>share
                                            </IconButton>
                                            <IconButton class="material-icons"
                                                        on:click={() => download_knime(element)}>download
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

        <div>
            <Button on:click={download_all_rdf} variant="outlined">
                <Label>Download all RDF representations</Label>
            </Button>
            <Button on:click={download_all_knime} variant="outlined">
                <Label>Download all KNIME representations</Label>
            </Button>
        </div>
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