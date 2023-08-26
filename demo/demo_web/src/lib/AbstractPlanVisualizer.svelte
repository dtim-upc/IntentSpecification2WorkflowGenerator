<script lang="ts">
    import {Background, Node, Svelvet} from 'svelvet';
    import {createEventDispatcher} from 'svelte';
    import {plan_layout} from './utils'
    import CircularProgress from "@smui/circular-progress";

    const dispatch = createEventDispatcher();

    export let plan: { [key: string]: string[] };
    export let plan_id: string;

    let nodes: any[];
    let edges: any[];
    let initialPosition: any;

    async function initialize() {
        let layout = await plan_layout(plan);
        nodes = layout.nodes;
        for (let node of nodes) {
            node.incoming = [];
            node.outgoing = [];
        }
        edges = layout.edges;
        for (let edge of edges) {
            let s = edge.source.split('#').at(-1)!;
            let t = edge.target.split('#').at(-1)!;
            nodes.find(n => n.id == edge.source).outgoing.push(t);
            nodes.find(n => n.id == edge.target).incoming.push(s);
        }
        console.log(nodes);
        console.log(edges);
    }

    let initializing = initialize();
</script>

<div>
    <h2 id="fullscreen-title">{plan_id.split('#').at(-1)}</h2>
    {#await initializing}
        <CircularProgress style="height: 32px; width: 32px;" indeterminate/>
    {:then _}
        <div id="canvas-div">
            <Svelvet controls>
                {#each nodes as node}
                    <Node id={node.data.label} label={node.data.label} position={{x: node.x, y:node.y}}
                          dimensions={{width: node.width, height: node.height}}
                          connections={node.outgoing}>
                    </Node>
                {/each}
                <Background dotColor="transparent" slot="background"/>
            </Svelvet>
        </div>
    {/await}
</div>

<style>
    #canvas-div {
        height: 60vh;
    }
</style>