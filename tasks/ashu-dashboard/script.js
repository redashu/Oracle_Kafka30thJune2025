let instanceStates = {};  // instance_id → state
let instanceRows = {};    // instance_id → table row

console.log("🔌 Connecting to WebSocket...");
const socket = new WebSocket("ws://13.250.18.50:8081/ws/ec2");

socket.onopen = () => console.log("✅ WebSocket connected!");

socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    const id = data.instance_id;
    const name = data.name || "Unnamed";
    const state = data.state;
    const ts = data.timestamp;

    const prevState = instanceStates[id];
    instanceStates[id] = state;

    // Remove from old state table if state changed
    if (prevState && prevState !== state && instanceRows[id]) {
        instanceRows[id].remove();
        delete instanceRows[id];
    }

    const tbody = document.getElementById(`${state}-body`);
    let row = instanceRows[id];

    if (!row) {
        row = document.createElement("tr");

        const nameCell = document.createElement("td");
        const idCell = document.createElement("td");
        const timeCell = document.createElement("td");

        nameCell.textContent = name;
        idCell.textContent = id;
        timeCell.textContent = formatTimestamp(ts);

        row.appendChild(nameCell);
        row.appendChild(idCell);
        row.appendChild(timeCell);

        tbody.appendChild(row);
        instanceRows[id] = row;
    } else {
        row.children[0].textContent = name;
        row.children[2].textContent = formatTimestamp(ts);
    }

    updateCounts();
};

function formatTimestamp(ts) {
    const d = new Date(ts);
    return d.toLocaleString();
}

function updateCounts() {
    const counts = { running: 0, stopped: 0, terminated: 0 };
    for (const state of Object.values(instanceStates)) {
        if (counts[state] !== undefined) counts[state]++;
    }
    document.getElementById("running-count").textContent = counts.running;
    document.getElementById("stopped-count").textContent = counts.stopped;
    document.getElementById("terminated-count").textContent = counts.terminated;
}
