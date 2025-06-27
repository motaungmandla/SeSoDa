\usepackage[utf8]{inputenc}




margin=1in







\maketitle


This paper presents the first well-structured and context-rich dataset for the Sesotho language. It includes culturally relevant expressions, idioms, and conversations. Designed for NLP researchers, this dataset is intended to support language modeling, translation, and chatbot development in a low-resource setting.




§ MOTIVATION

[noitemsep]
    \item
Create ready to use dataset for the Sesotho language 
    \item
Sesotho is underrepresented in the field and we're attempting to fix that
    \item
 Preserve and digitize nuanced Sesotho vocabulary, including idioms, proverbs, and metaphors.
    \item Enable NLP/ML research for low-resource African languages.
    \item
Trying to make AI more useful to all without language being a barrier 

    \item Capture social and cultural contexts missing from existing resources.
    \item Build a foundation for open-source Sesotho assistants and educational tools.




§ DATASET FORMAT

Format: JSON Lines (.jsonl)\\
Each line is a structured JSON object:

{
  "prompt": "Sesotho phrase",
  "completion": "Meaning/translation",
  "type": "noun/verb/idiom/etc",
  "category": "semantic theme",
  "metadata": {
    "context": "cultural or emotional",
    "example": "usage sentence"
  }
}




§ STATISTICS




    \item Total Entries: [X]
    \item File Size: [Y MB]

\item Unique Linguistic Types: noun, verb, idiom, etc.




§ EVALUATION

Initial evaluation was done by:

    \item Human reviewers (fluency, clarity)
    \item Sampled prompts tested with Qwen-0.5B
    \item Manual validation of translation and structure




§ USE CASES


    \item Conversational AI in Sesotho
    \item Language learning platforms
    \item Cultural and linguistic preservation
    \item Fine-tuning foundational LLMs
     \item
Laying foundations for Sesotho based AI agents




§ LIMITATIONS


    \item Limited coverage of dialects
    \item Context annotations are ongoing
    \item Dataset currently focused on standard and formal Sesotho




§ RESOURCES AND TOOLS


    \item Python, kaggle datasets, Hugging Face Datasets
    \item Data sources: , Tutudu hae patwe novel, Lejwe la kgupiso story book, melodi ya di thothokiso, NMDS Facebook page, Sesotho texts from the web
    \item Related Work: Masakhane, Common Voice, BLOOM, Deep learning Indaba.




§ DOWNLOAD

Dataset available at: <https://github.com/motaungmandla/zmmandla.github.io/webscrap.jsonl>
