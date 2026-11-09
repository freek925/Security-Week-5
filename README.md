# Security Week 5

# De Text Encryptinator

## 1. Introductie

De Text Encryptinator is een consoleapplicatie waarmee gebruikers tekst kunnen versleutelen en ontsleutelen met behulp
van een wachtwoord. De applicatie is ontwikkeld met Python en maakt gebruik van symmetrische encryptie.

Het doel van dit project is om meer inzicht te krijgen in hoe encryptie werkt en hoe cryptografische sleutels veilig
kunnen worden beheerd.

## 2. Installatie en gebruik

### 2.1. Installatie

Om de applicatie te gebruiken, moet Python geïnstalleerd zijn. Vervolgens kunnen de benodigde dependencies worden
geïnstalleerd met:

```bash
pip install -r requirements.txt
```

Daarna kan de applicatie worden gestart met:

```bash
python main.py
```

### 2.2. Gebruik

Na het starten van de applicatie verschijnt een menu met drie opties:

1. Encrypt text: De gebruiker voert tekst en een wachtwoord in. De applicatie versleutelt de tekst en geeft het
   resultaat terug als een Base64-gecodeerde string.
2. Decrypt text: De gebruiker voert een eerder versleutelde tekst en het bijbehorende wachtwoord in. Als het wachtwoord
   correct is, wordt de oorspronkelijke tekst weergegeven.
3. Exit: Sluit de applicatie af.

Voor het ontsleutelen moet hetzelfde wachtwoord worden gebruikt als bij het versleutelen (duh). Bij een verkeerd
wachtwoord of ongeldige versleutelde tekst geeft de applicatie een foutmelding.

## 3. Symmetrische en asymmetrische encryptie

### 3.1. Symmetrische encryptie

Bij symmetrische encryptie wordt dezelfde sleutel gebruikt voor zowel het versleutelen als het ontsleutelen van
gegevens. Dit maakt symmetrische encryptie relatief snel en geschikt voor het versleutelen van grote hoeveelheden data.

Het nadeel hiervan is wel dat beide partijen over dezelfde geheime sleutel moeten beschikken. Wanneer versleutelde
gegevens met iemand anders worden gedeeld, moet de sleutel dus eerste ook op een veilige manier zijn uitgewisseld.

Voorbeelden van symmetrische encryptiealgoritmen zijn [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
en [ChaCha20](https://proton.me/learn/encryption/glossary/chacha20).

### 3.2. Asymmetrische encryptie

Bij asymmetrische encryptie wordt gebruikgemaakt van twee verschillende sleutels: een publieke sleutel en een
privésleutel. De publieke sleutel kan met anderen worden gedeeld, terwijl de privésleutel geheim moet blijven.

Bij asymmetrische versleuteling kan iemand gegevens versleutelen met de publieke sleutel van de ontvanger. Alleen de
bijbehorende privésleutel kan deze gegevens weer ontsleutelen.

Een voordeel hiervan is dat er vooraf geen geheime sleutel hoeft te worden uitgewisseld. Asymmetrische encryptie is
doorgaans wel langzamer en meer resource intensive dan symmetrische encryptie.

Een voorbeeld van een asymmetrisch encryptiealgoritme is [RSA](https://en.wikipedia.org/wiki/RSA_cryptosystem).

## 4. Implementatie en encryptiealgoritme

### 4.1. AES-256-GCM

Voor de applicatie heb ik gekozen voor AES-256 in GCM-modus. AES is een veelgebruikt symmetrisch encryptiealgoritme.

GCM is een vorm van authenticated encryption. Dit betekent dat naast het versleutelen van de gegeven ook de integriteit
wordt gecontroleerd. Hierdoor kan de applicatie detecteren wanneer de versleutelde gegevens zijn aagepast of met een
verkeerde sleutel worden ontsleuteld.

AES-256-GCM is gekozen omdat het een modern en veilig algoritme is dat zowel betrouwbaarheid als integriteit biedt.

### 4.2. Implementatie in Python

Voor de implementatie wordt gebruikgemaakt van de Python-library [cryptography](https://cryptography.io/en/latest/).
Hiermee hoef ik de cryptografische werking van AES niet zelf te implementeren (Don't roll your own crypto).

Bij het versleutelen genereert de applicatie een willekeurige salt van 16 bytes en een nonce (number used once) van 12
bytes. De salt wordt gebruikt bij het afleiden van de encryptiesleutel en de nonce zorgt ervoor dat AES-GCM niet telkens
met dezelfde combinatie van sleutel en nonce wordt uitgevoerd.

Vervolgens wordt de tekst versleuteld met AESGCM.encrypt(). De salt, nonce en versleutelde gegevens worden samengevoegd
en omgezet naar een Base64-string, zodat het resultaat eenvoudig gekopieerd kan worden.

Bij het ontsleutelen wordt dit proces omgekeerd. De applicatie haalt de salt en nonce uit de Base64-string en gebruikt
deze om de oorspronkelijke tekst te herstellen. Wanneer de authenticatie mislukt, wordt een foutmelding weergegeven.

## 5. Sleutelbeheer

### 5.1 Sleutelgeneratie

De applicatie gebruikt geen vooraf ingestelde encryptiesleutel, maar leidt deze af van het wachtwoord dat de gebruiker
invoert. Hiervoor wordt gebruikgemaakt van de Scrypt key derivation functie.
Bij iedere versleuteling wordt een willekeurige salt van 16 bytes gegenereerd. Scrypt gebruikt deze salt samen met het
wachtwoord om een AES-sleutel van 256 bits af te leiden. Hierdoor levert hetzelfde wachtwoord bij verschillende
versleutelingen niet dezelfde sleutel op.
Scrypt is ontworpen om relatief veel rekenkracht en geheugen te gebruiken, waardoor het voor aanvallers moeilijker wordt
om grote aantallen wachtwoorden uit te proberen.

### 5.2 Sleutelopslag

De applicatie slaat het wachtwoord en de afgeleide encryptiesleutel niet permanent op. Bij het ontsleutelen wordt de
sleutel opnieuw afgeleid met het ingevoerde wachtwoord en de oorspronkelijke salt.
De salt en nonce worden samen met de versleutelde tekst opgeslagen in de Base64-string. Deze waarden hoeven niet geheim
te blijven. Alleen het wachtwoord en de daarvan afgeleide sleutel moeten geheim blijven (Shoutout naar Kerckhoff).
Een nadeel van deze aanpak is dat de versleutelde tekst niet meer ontsleuteld kan worden wanneer het wachtwoord verloren
gaat.

### 5.3 Sleuteluitwisseling en beveiligingsrisico's

Wanneer een gebruiker versleutelde tekst met iemand anders wil delen, moet de ontvanger ook over het juiste wachtwoord
beschikken.
Dit vormt een beveiligingsrisico, omdat het wachtwoord onderschept kan worden wanneer het via een onbeveiligd kanaal
wordt gedeeld. Een mogelijke oplossing is om het wachtwoord via een ander, beveiligd communicatiekanaal uit te wisselen.
Bij een groot aantal gebruikers wordt
dit [steeds ingewikkelder](https://nl.wikipedia.org/wiki/Binomiaalco%C3%ABffici%C3%ABnt). Iedere gebruiker moet de
juiste wachtwoorden veilig
ontvangen en beheren. Dit maakt symmetrische encryptie minder praktisch wanneer veel verschillende gebruikers onderling
versleutelde berichten willen uitwisselen.
Daarnaast is de beveiliging afhankelijk van de sterkte van het gekozen wachtwoord. Ondanks het gebruik van scrypt kunnen
zwakke wachtwoorden nog steeds worden achterhaald door middel van wachtwoordaanvallen.

### 6. Principe van Kerkhoffs

Het Principe van Kerkhoffs stelt dat een cryptografisch systeem veilig moet blijven, zelfs wanneer de volledige werking
ervan openbaar is. Alleen de geheime sleutel mag noodzakelijk zijn om de beveiliging te behouden.

Text Encryptinator volgt dit principe door gebruik te maken van bestaande en openbaar gedocumenteerde cryptografisch
algoritmen.

De beveiliging is hierdoor niet afhankelijk van het geheimhouden van de implementatie, maar van het wachtwoord dat de
gebruiker kiest. Ook de salt en de nonce hoeven niet geheim te blijven en worden daarom samen met de versleutelde tekst
opgeslagen.

Wanneer een aanvaller toegang heeft tot de volledige broncode en de versleutelde gegevens, zou deze zonder het juiste
wachtwoord de oorspronkelijke tekst niet moeten kunnen achterhalen. Dit is wel natuurlijk wel afhankelijk van de sterkte
van het gebruikte wachtwoord.
