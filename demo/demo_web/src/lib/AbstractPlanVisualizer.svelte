<script>
    import Dialog, { Header, Title, Content } from '@smui/dialog';
    import { Svelvet, Node, Anchor, Edge, Controls } from 'svelvet';
    import {createEventDispatcher} from 'svelte';

    const dispatch = createEventDispatcher();

    export let open = false;
    export let plan;

    let nodes = [];

    for (let node of nodes) {

    }
</script>

<Dialog
        bind:open
        fullscreen
        aria-labelledby="fullscreen-title"
        aria-describedby="fullscreen-content"
        on:SMUIDialog:closed={() => dispatch('close')}
>
    <Header>
        <Title id="fullscreen-title">Abstract Plan</Title>
    </Header>
    <Content id="fullscreen-content">
        <Svelvet width={1000} height={500} nodes={nodes}>
        </Svelvet>
    </Content>
</Dialog>