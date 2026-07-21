from langchain.chains.llm import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from genosclient.langchain_plugin import jsguruGenAIChatV2


def langchain_chat():
    chat = jsguruGenAIChatV2(
        temperature=0,
        metadata={
            # mandetory field
            "experience_id": EXPERIENCE_ID,
            # for authn/authz
            # not required for experiments
            # "env": "<prd or e2e>", # default value is e2e
            # "app_id": "<>",
            # "app_secret": "<>",
            # "auth_id": "<>",
            # "ticket": "<>"
            # "jsguru_originating_assetalias": "<>"
        },
        model_name="gpt-35-turbo",
    )

    template = "You are a helpful assistant that translates {input_language} to {output_language}."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    res = chain.invoke(
        input={
            "input_language": "English",
            "output_language": "French",
            "text": "I love programming.",
        }
    )
    print(res)


async def langchain_achat():
    chat = jsguruGenAIChatV2(
        temperature=0,
        metadata={
            # mandetory field
            "experience_id": EXPERIENCE_ID,
            # needed only for chat-film
            # "version": "2",
            # for authn/authz
            # not required for experiments
            # "env": "<prd or e2e>", # default value is e2e
            # "app_id": "<>",
            # "app_secret": "<>",
            # "auth_id": "<>",
            # "ticket": "<>"
        },
        model_name="gpt-35-turbo",
    )

    template = "You are a helpful assistant that translates {input_language} to {output_language}."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    res = await chain.ainvoke(
        input={
            "input_language": "English",
            "output_language": "French",
            "text": "I love programming.",
        }
    )
    print(res)