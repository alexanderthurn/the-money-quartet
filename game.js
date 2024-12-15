document.addEventListener('DOMContentLoaded', () => {
    fetch('currencies.json')
        .then(response => response.json())
        .then(data => {
            displayCards(data);
        })
        .catch(error => console.error('Error loading data:', error));
});

function displayCards(currencies) {
    const container = document.getElementById('card-container');
    const template = document.getElementById('card-template');

    currencies.forEach(currency => {
        const card = template.content.cloneNode(true);

        // Titel setzen
        const title = card.querySelector('.title');
        title.textContent = currency.name;

        // Bild setzen
        const imagePlaceholder = card.querySelector('.image-placeholder');
        const className = 'card_' + currency.id;
        imagePlaceholder.classList.add(className);

        // Attribute setzen
        const attributesDiv = card.querySelector('.attributes');
        attributesDiv.innerHTML = `
            <div class="attribute">
                <span>Since: ${currency.since}</span>
                <div class="progress-bar"><div style="width: 100%;"></div></div>
            </div>
            <div class="attribute">
                <span>Scarcity: ${currency.scarcity}</span>
                <div class="progress-bar"><div style="width: ${(currency.scarcity / 5) * 100}%"></div></div>
            </div>
            <div class="attribute">
                <span>Durability: ${currency.durability}</span>
                <div class="progress-bar"><div style="width: ${(currency.durability / 5) * 100}%"></div></div>
            </div>
            <div class="attribute">
                <span>Divisibility: ${currency.divisibility}</span>
                <div class="progress-bar"><div style="width: ${(currency.divisibility / 5) * 100}%"></div></div>
            </div>
            <div class="attribute">
                <span>Transportability: ${currency.transportability}</span>
                <div class="progress-bar"><div style="width: ${(currency.transportability / 5) * 100}%"></div></div>
            </div>
        `;

        // Beschreibung setzen
        const description = card.querySelector('.description');
        description.textContent = currency.description;


        description.addEventListener('click', () => {
            card.classList.toggle('flipped');
        });

        // Karte zum Container hinzufügen
        container.appendChild(card);

        const cards = document.querySelectorAll('.card');

    });
}