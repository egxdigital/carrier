from carrier.config import EMAIL

my_address = (
    "<b>Emille Giddings</b>\n"
    "938 Section A Block X Great Diamond\n"
    "East Bank Demerara\n"
    "(592) 647-5005\n"
)

kaieteur_address = (
    "Kaieteur News\n"
    "24 Saffon St.\n"
    "Charlestown\n"
    "Georgetown\n"
)

stabroek_address = (
    "Stabroek News\n"
    "46-47 Robb Street\n"
    "Lacytown\n"
    "Georgetown, Guyana\n"
)

chronicle_address = (
    "Guyana Chronicle\n"
    "Lama Avenue\n"
    "Bel Air Park\n"
    "Georgetown, Guyana\n"
)

guyanatimes_address = (
    "Guyana Times Inc\n"
    "Queens Atlantic Industrial Estate, Ruimveldt\n"
    "Georgetown, Guyana\n"
)

inewsgy_address = (
    "Queens Atlantic Investment Inc.\n"
    "Industrial Estate, Ruimveldt\n"
    "Georgetown, Guyana.\n"
)

demwaves_address = (
    "Demerara Waves\n"
    "CIDA Programme Support Building\n"
    "Georgetown, Guyana.\n"
)

newsroom_address = (
    "News Room\n"
    "Lot 291 Thomas Street\n"
    "South Cummingsburg\n"
    "Georgetown, Guyana.\n"
)

oilnow_address = (
    "OilNOW\n"
    "Guyana\n"
)

village_voice_address = {
    "Village Voice News\n"
    "X-Y Woolford Avenue, Thomas Lands\n"
    "Georgetown, Guyana\n"
}

letter_to_editor = (
    "{my_address}\n"
    "{date}\n"
    "\n"
    "<b>The Editor</b>\n"
    "{tabloid_address}"
    "\n"
    "Dear Editor,\n"
    "{message}"
    "Sincerely,\n"
    "Emille Giddings\n"
)

credential = "Software Developer | Specialized Management Software for Small-Medium Sized Businesses in Guyana\n"

email_message_to_editor = (
    "Editor,\n"
    "\n"
    "See attached for my letter dated {Month} {day}.\n"
    "\n"
    "Regards,\n"
)

email_message_to_editor_with_credentials = (
    "Editor,\n"
    "\n"
    "See attached for my letter dated {Month} {day}.\n"
    "\n"
    "Regards,\n"
    "Emille Giddings\n"
    f"{credential}"
)

email_message_to_editor_with_edits = (
    "Editor,\n"
    "\n"
    "For what it's worth, I've added a few small tweaks to my letter already in your inbox.\n"
    "\n"
    "I understand if this message either comes too late or is not relevant.\n"
    "\n"
    "I am sorry for any inconvenience caused.\n"
    "\n"
    "See attached for my updated letter dated {Month} {day}\n"
)

addresses = {
    'stabroek': stabroek_address,
    'kaieteur': kaieteur_address,
    'chronicle': chronicle_address,
    'guyanatimes': guyanatimes_address,
    'inewsgy': inewsgy_address,
    'demwaves': demwaves_address,
    'newsroom': newsroom_address,
    'oilnow': oilnow_address,
    'village_voice': village_voice_address,
    'engineer': my_address,
    'dummytabloid': "12 Hatter Lane, Through the Rabbit Hole"
}

emails = {
    'engineer': EMAIL,
    'stabroek': 'stabroeknews@stabroeknews.com',
    'kaieteur': 'kaieteurnews@yahoo.com',
    'chronicle': 'gnnleditorial@gmail.com ',
    'guyanatimes': 'news@guyanatimesgy.com',
    'inewsgy': 'inewsgy@gmail.com',
    'demwaves': 'dchabrol@demerarawaves.com',
    'newsroom': 'news@newsroom.gy',
    'oilnow': 'editor@oilnow.gy',
    'village_voice': 'wnigel10@hotmail.com'
}
