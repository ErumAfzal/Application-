import streamlit as st

# German Language Learning App

st.set_page_config(page_title="Deutsch Lern-Bot", page_icon="🇩🇪", layout="centered")

st.title(" Deutsch Lern-Bot – Dein interaktiver Sprachhelfer")
st.write("Ich bin dein KI-Tutor, ein deutscher Muttersprachler, der dir beim Deutschlernen hilft. ")

# Step 1: Select level
level = st.selectbox("Wähle dein Sprachniveau:", ["A1", "A2"])

# Step 2: Select topic
topics = {
    "A1": ["Begrüßungen", "Wortschatz", "Hören", "Schreiben", "Lesen"],
    "A2": ["Begrüßungen", "Wortschatz", "Hören", "Schreiben", "Lesen"]
}
topic = st.selectbox("Was möchtest du lernen?", topics[level])

# Step 3: Show content
def get_content(level, topic):
    if level == "A1":
        if topic == "Begrüßungen":
            return """
### Begrüßungen (A1)

| Deutsch        | Englisch     |
|----------------|--------------|
| Hallo!         | Hello!       |
| Guten Morgen!  | Good morning!|
| Guten Tag!     | Good day!    |
| Guten Abend!   | Good evening!|
| Wie geht's?    | How are you? |
            """
        elif topic == "Wortschatz":
            return """
###  Wortschatz (A1)

- Ich heiße Anna.
- Ich komme aus Deutschland.
- Ich wohne in Berlin.
- Ich spreche ein bisschen Deutsch.
- Das ist mein Freund.

Tipp: Wiederhole jeden Satz laut.
            """
        elif topic == "Hören":
            return """
### 🎧 Hörverstehen (A1)

 **Audio-Satz:** „Guten Morgen, ich heiße Thomas.“  
 Frage: Was ist der Name der Person?

🔉 Du kannst [diese Übung anhören](https://www.schubert-verlag.de/aufgaben/uebungen_a1/a1_hoeren.htm)
            """
        elif topic == "Schreiben":
            return """
### ✍️ Schreiben (A1)

**Aufgabe:**  
Schreibe einen kurzen Text über dich (3–4 Sätze).  
Beispiel:  
> Ich heiße Maria.  
> Ich komme aus Spanien.  
> Ich bin 25 Jahre alt.  
> Ich lerne Deutsch.

Du kannst deinen Text unten eingeben:
"""
        elif topic == "Lesen":
            return """
### 📖 Leseverstehen (A1)

**Text:**  
> Hallo! Ich heiße Ben. Ich bin 20 Jahre alt und wohne in Hamburg. Ich lerne Deutsch und spiele gerne Fußball.

 Frage: Wo wohnt Ben?  
**Antwortmöglichkeiten:**  
- Berlin  
- München  
- **Hamburg** ✅
            """

    elif level == "A2":
        if topic == "Begrüßungen":
            return """
### 👋 Begrüßungen (A2)

- Schön, dich zu sehen!
- Lange nicht gesehen!
- Wie war dein Wochenende?
- Was gibt’s Neues?

 Achte auf die Höflichkeitsformen in verschiedenen Situationen.
            """
        elif topic == "Wortschatz":
            return """
### Wortschatz (A2)

- Ich interessiere mich für Musik.
- Ich arbeite als Ingenieurin.
- Mein Lieblingsessen ist Pizza.
- Ich möchte Deutsch fließend sprechen.

 Nutze neue Wörter in eigenen Sätzen!
            """
        elif topic == "Hören":
            return """
###  Hörverstehen (A2)

 **Dialog:** Zwei Personen sprechen über ihre Urlaubspläne.  
 Ziel: Verstehe den Inhalt und beantworte Fragen.

[Hier kannst du Übungen finden](https://learngerman.dw.com/de/a2-hoeren/s-13306)
            """
        elif topic == "Schreiben":
            return """
###  Schreiben (A2)

**Aufgabe:**  
Schreibe eine E-Mail an einen Freund und erzähle von deinem Wochenende. (5–6 Sätze)

Beispiel:  
> Am Samstag war ich im Kino. Der Film war spannend. Am Sonntag habe ich gekocht und Deutsch gelernt.
            """
        elif topic == "Lesen":
            return """
### 📖 Leseverstehen (A2)

**Text:**  
> Am Freitag hat Maria Geburtstag gefeiert. Viele Freunde waren da. Es gab Kuchen und Musik. Alle hatten Spaß.

 Frage: Was wurde gefeiert?  
**Antwort:** Marias Geburtstag 🎂
            """

    return "Inhalt folgt bald."

st.markdown(get_content(level, topic), unsafe_allow_html=True)

if topic == "Schreiben" and level in ["A1", "A2"]:
    user_text = st.text_area("✍Schreib hier deinen Text:")
    if user_text:
        st.success("Danke für deinen Text! Du kannst ihn einem Lehrer oder Tutor zeigen.")
