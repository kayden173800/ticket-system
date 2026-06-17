async function createTicket() {
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;

    await fetch("/tickets", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ title, description })
    });

    loadTickets();
}

async function loadTickets() {
    const res = await fetch("/tickets");
    const data = await res.json();

    let html = "";

    data.forEach(ticket => {
        html += `
        <div class="ticket">
            <h3>${ticket[1]}</h3>
            <p>${ticket[2]}</p>
            <small>Status: ${ticket[3]}</small>
            <hr>
        </div>
        `;
    });

    document.getElementById("tickets").innerHTML = html;
}

loadTickets();