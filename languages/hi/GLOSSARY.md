# Hindi (hi) glossary

## Register

- **App and agent to the person: "आप"**, with the polite imperative (करें, देखें, चुनें). This is what popular Indian apps use (Google, WhatsApp, Paytm, PhonePe).
- **What the person says to their agent: "तुम" imperative** (करो, दो, बताओ). This is how people really talk to an assistant: "मेरे ब्रेन का चेक-अप करो". Trigger phrases use this form, followed by the English phrase.
- **Rule files written for the agent** (`CLAUDE.md`, skill files) use the polite imperative (पढ़ें, लिखें), same as the app voice.
- **Gender:** Hindi verbs show gender. Form options and examples are worded so they work for anyone (no "करता/करती" slashes). The agent's own lines avoid gendered verbs where possible ("अभी मैं किसके साथ काम करूँ?").
- Everyday Hindi with the English loanwords people really use in apps: फ़ाइल, फ़ोल्डर, नोट, लिंक, प्रोजेक्ट, क्लाइंट, टूल, ऐप, बैकअप, रिपोर्ट, चैट, ईमेल, सेटअप. No Sanskritised words where a common one exists (लक्ष्य is fine, उद्देश्य-पूर्ति is not).
- Nukta used consistently: फ़ाइल, फ़ैसला, ज़रूरी, ख़ास, क़तार, तारीख़.
- Number words stay as digits. Danda (।) ends sentences; question mark as usual.

## Feature names

| English | Hindi | Why |
|---|---|---|
| Phygital Brain | Phygital Brain | Product name, stays English |
| Brain Keeper | ब्रेन कीपर | Transliterated, works as a name; "रखवाला" sounded childish |
| morning brief | मॉर्निंग ब्रीफ़ | Common in Indian office Hinglish; trigger "मॉर्निंग ब्रीफ़ दो" |
| meeting prep | मीटिंग की तैयारी | Natural phrase; trigger "{name} से मीटिंग की तैयारी करवाओ" |
| thinking tools | सोचने के टूल | Plain |
| check-up | चेक-अप | Everyone says it (doctor's check-up) |
| Writing Check | राइटिंग चेक | Short, clear as a feature name |
| second brain | सेकंड ब्रेन | "दूसरा दिमाग़" reads like a joke; "ब्रेन" is used for the folder everywhere |
| your agent | आपका एजेंट | |

## Folder and note names

Hindi has no capital letters, so top folders are just the word. Words in a name are joined with hyphens.

| English | Hindi | English | Hindi |
|---|---|---|---|
| About | परिचय | Daily | रोज़ाना |
| Projects | प्रोजेक्ट | Relationships | संपर्क |
| Memory | याददाश्त | Library | लाइब्रेरी |
| Skills | स्किल | Clients | क्लाइंट |
| Collaborators | सहयोगी | Team | टीम |
| Partners | पार्टनर | decisions | फ़ैसले |
| research | रिसर्च | finances | हिसाब-किताब |
| archive | आर्काइव | applications | आवेदन |
| competitors | प्रतिस्पर्धी | notes | नोट्स |
| briefs | ब्रीफ़ | drafts | ड्राफ़्ट |
| ideas | आइडिया | feedback | फ़ीडबैक |
| assets | मीडिया | prompts | प्रॉम्प्ट |
| templates | टेम्पलेट | frameworks | फ़्रेमवर्क |
| brain-keeper | ब्रेन-कीपर | morning-brief | मॉर्निंग-ब्रीफ़ |
| meeting-prep | मीटिंग-की-तैयारी | thinking | सोच-विचार |
| import | इम्पोर्ट | connected-apps | जुड़े-ऐप |
| reports | रिपोर्ट | me | मैं |
| goals | लक्ष्य | business | बिज़नेस |
| services | सेवाएँ | customers | ग्राहक |
| pain-points | परेशानियाँ | brand | ब्रांड |
| tools | टूल | cv | सीवी |
| biography | जीवनी | tasks | टू-डू |
| _Leads | _लीड | daily (Brain Keeper's daily run file) | रोज़-की-सफ़ाई |
| check-up | चेक-अप | queue | क़तार |
| PAUSED | रुका-हुआ | | |

Notes on choices:
- **Relationships → संपर्क** ("contacts"). "रिश्ते" sounds like family; this folder is clients, collaborators, team and partners.
- **Memory → याददाश्त**, not "यादें" (which means fond memories).
- **finances → हिसाब-किताब**, the everyday word for keeping track of money.
- **tasks → टू-डू**, because "काम" also means "work" and would be confusing next to everything else.
- **Brain Keeper's `daily.md` → रोज़-की-सफ़ाई** ("daily tidy"), so it isn't confused with the `Daily` folder (रोज़ाना).
- **assets → मीडिया**: the folder holds images and media.

## Terms fixed in the text

| English | Hindi |
|---|---|
| info block (frontmatter) | इन्फ़ो ब्लॉक (frontmatter) |
| daily note | रोज़ का नोट |
| open tasks | बाकी काम |
| root rule 9 | मुख्य नियम 9 |
| the root `CLAUDE.md` | मुख्य `CLAUDE.md` |
| compiled-truth format | ताज़ा-सच फ़ॉर्मेट (ऊपर आज का सच, नीचे तारीख़ वाले सबूत) |
| Evidence (section) | सबूत |
| Knowledge Routing (section) | जानकारी कहाँ जाए |
| routing table | "कहाँ क्या जाए" टेबल |
| Backups and Undo (section) | बैकअप और वापस लेना |
| {Name}'s Rules (section) | {Name} के नियम |
| What it is / Status and next step | यह क्या है / स्टेटस और अगला कदम |
| How it runs / Where things are | यह कैसे चलता है / कौन-सी चीज़ कहाँ है |
| Rules per project | हर प्रोजेक्ट के अपने नियम |
| lead / New / Keep warm | लीड / नई / संपर्क बनाए रखें |
| queue: Last run / Needs {Name} / To fix / Next folder | पिछला रन / {Name} के फ़ैसले का इंतज़ार / ठीक करना है / अगला फ़ोल्डर |
| report: Summary / Files changed / Fixed / Queued / Errors | सारांश / बदली गई फ़ाइलें / ठीक किया / क़तार में डाला / गड़बड़ियाँ |
| Open decisions / From your apps / Meetings | खुले फ़ैसले / आपके ऐप से / मीटिंग |
| (from email) / (from calendar) | (ईमेल से) / (कैलेंडर से) |
| needs review | दोबारा देखना है |
| dry run | ड्राई रन |
| tidy (my brain) | साफ़-सुथरा करना (not "ठीक-ठाक", which also means "so-so") |
| Friendly and casual / Formal / Playful (form) | दोस्ताना और कैज़ुअल / फ़ॉर्मल / मज़ेदार (what apps say; "चुलबुला" sounds flirty) |
| orphan note | अनाथ नोट |
| broken link | टूटा लिंक |
| safe fixes / report only (Fix mode values) | stay in English, they're settings values |
| em dash | em dash (लंबा डैश) |
| session log | सेशन लॉग |
| wikilinks | विकिलिंक (`[[wikilinks]]` in code stays) |
| work days | कामकाजी दिन |
| Mon to Sun | सोम, मंगल, बुध, गुरु, शुक्र, शनि, रवि |

## Example names

Local names, used the same way everywhere: Ana Costa → अनन्या शर्मा, Marta → मीरा, João → राहुल, Lia → लता, Lisbon, Portugal → पुणे, भारत. In the social media example, TikTok (blocked in India) became YouTube.
