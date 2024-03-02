Mijn applicatie is een ticketsysteem voor de ICT-helpdesk van een organisatie. Met deze applicatie worden ICT-problemen geregistreerd.

De applicatie kent twee typen gebruikers:

Gewone gebruikers: Zij kunnen ICT-meldingen aanmaken via de website. Daarnaast kunnen ze eerdere meldingen bekijken en de status van hun meldingen monitoren.
Behandelaars: Dit zijn de leden van het ICT-helpdeskteam. Zij kunnen de meldingen van gebruikers bekijken, eventuele oplossingen toevoegen en de tickets behandelen. Daarnaast hebben ze toegang tot trends van meldingen in grafiekvorm.
Voor de twee typen gebruikers zijn er twee verschillende inlogschermen. Gewone gebruikers kunnen inloggen met hun e-mailadres en wachtwoord. Behandelaars moeten ook tweestapsverificatie gebruiken om in te loggen.

Op het dashboard van gewone gebruikers kunnen ze:

Hun eigen meldingen bekijken en de status ervan controleren.
Een nieuwe melding aanmaken.
Admin gebruikers kunnen op hun dashboard:

De meldingen van gebruikers bekijken en behandelen.
Trends van de meldingen als grafiek bekijken.
In mijn project zijn er twee tabellen:

Gebruikers
Tickets
Hierbij heb ik een one-to-many relatie gebruikt. Elke gebruiker kan meerdere tickets hebben.
Voor CSS heb ik voornamelijk Bootstrap gebruikt in plaats van vanilla CSS.

JavaScript wordt gebruikt voor data-analyse (met CanvasJS), AJAX-requests en voor het weergeven van waarschuwingsberichten (met SweetAlert).
