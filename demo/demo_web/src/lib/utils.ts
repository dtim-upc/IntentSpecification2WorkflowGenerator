import ELK from 'elkjs/lib/elk.bundled.js'

const elk = new ELK()

export {plan_layout, removeLastPart, windowsStyleSort};

function removeLastPart(inputString: string): string {
    const parts = inputString.split(' ');

    if (parts.length > 1) {
        parts.pop(); // Remove the last part
        return parts.join(' ');
    } else {
        return inputString; // Return the original string if there's only one part
    }
}

function windowsStyleSort(strings: string[]): string[] {
    return strings.slice().sort((a, b) => {
        return a.localeCompare(b, undefined, {numeric: true, sensitivity: 'base'});
    });
}

async function plan_layout(plan: { [key: string]: string[] }) {
    let nodes = Object.keys(plan).map(node => {
        let label = node.split('#').at(-1)!;
        return {
            id: node,
            data: {
                label: label,
            },
            width: label.length * 10 > 50 ? label.length * 10 : 50,
            height: 50,
            sourcePosition: 'right',
            targetPosition: 'left',
        }
    });

    let edges = [];
    let i = 0;
    for (let source of Object.keys(plan)) {
        for (let target of plan[source]) {
            edges.push({
                id: 'e' + i,
                sources: [source],
                targets: [target],
                source: source,
                target: target,
                arrow: true,
            });
            i++;
        }
    }

    const graph = {
        id: "root",
        layoutOptions: {
            'elk.algorithm': 'layered',
            'elk.direction': 'org.eclipse.elk.core.options.Direction.DOWN'
        },
        children: nodes,
        edges: edges
    }

    const layout = await elk.layout(graph);

    return {
        nodes: layout.children!,
        edges: layout.edges || [],
    }

}