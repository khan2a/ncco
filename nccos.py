from datetime import datetime

# these urls are for testing and running code in replit or using local flask server
# SERVER_URL = "http://khan2a.com:8080"
# SERVER_URL = "https://rtc-amd-smokes.main0.api.rtc.dev.euw1.vonagenetworks.net"
# SERVER_URL = "https://py.khan2a.repl.co"
# SERVER_URL = "https://async-amd-eventurl.dev.nexmo.cloud"


#### NCCO Talk ####
def ncco_talk_if_human(event):
    return [
        {
            "action": "notify",
            "payload": {
                "event": "human",
                "action": "talk",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        # commented out but will be useful to test parallel recording
        #   {
        #     "action": "record",
        #     "eventUrl": [event["notify_event_url"]],
        #     # "format": "mp3", "split": "conversation", "channels": 2
        # },
        {
            "action": "talk",
            "voiceName": "Amy",
            "text": "I am talking to a human.",
            "level": 1,
            "loop": 10,
        },
    ]


def ncco_talk_if_machine(event):
    return [
        {
            "action": "notify",
            "payload": {
                "event": "machine",
                "action": "talk",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        # commented out but will be useful to test parallel recording
        #   {
        #     "action": "record",
        #     "eventUrl": [event["notify_event_url"]],
        #     # "format": "mp3", "split": "conversation", "channels": 2
        # },
        {
            "action": "talk",
            "voiceName": "Amy",
            "text": "I am talking to a machine before the beep.",
            "level": 1,
            "loop": 10,
        },
    ]


def ncco_talk_if_beep_start(event):
    return [
        {
            "action": "notify",
            "payload": {
                "event": "beep_start",
                "action": "talk",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        # commented out but will be useful to test parallel recording
        #   {
        #     "action": "record",
        #     "eventUrl": [event["notify_event_url"]],
        #     # "format": "mp3", "split": "conversation", "channels": 2
        # },
        {
            "action": "talk",
            "voiceName": "Amy",
            "text": "I am talking to a machine after the beep.",
            "level": 1,
            "loop": 3,
        },
    ]


def ncco_talk_if_fax(event):
    return [
        {
            "action": "notify",
            "payload": {
                "event": "fax",
                "action": "talk",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        # commented out but will be useful to test parallel recording
        #   {
        #     "action": "record",
        #     "eventUrl": [event["notify_event_url"]],
        #     # "format": "mp3", "split": "conversation", "channels": 2
        # },
        {
            "action": "talk",
            "voiceName": "Amy",
            "text": "I am talking to a fax machine.",
            "level": 1,
            "loop": 3,
        },
    ]


def ncco_talk_if_beep_timeout(event):
    return [
        {
            "action": "notify",
            "payload": {
                "event": "beep_timeout",
                "action": "talk",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        # commented out but will be useful to test parallel recording
        #   {
        #     "action": "record",
        #     "eventUrl": [event["notify_event_url"]],
        #     # "format": "mp3", "split": "conversation", "channels": 2
        # },
        {
            "action": "talk",
            "voiceName": "Amy",
            "text": "I am talking to a machine with beep timeout.",
            "level": 1,
            "loop": 3,
        },
    ]


#### NCCO Stream ####
def ncco_stream_if_human(event):
    return [
        {
            "action": "notify",
            "payload": {
                "event": "human",
                "action": "stream",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        {
            "action": "stream",
            "streamUrl": [
                "https://d227vfuz68nmz8.cloudfront.net/audio_files/test_smoke3_music-on-hold-ten.wav"
            ],
            "bargeIn": "false",
        },
    ]


def ncco_stream_if_machine(event):
    return [
        {
            "action": "notify",
            "payload": {
                "event": "machine",
                "action": "stream",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        # commented out but will be useful to test parallel recording
        #       {
        #     "action": "record",
        #     "eventUrl": [event["notify_event_url"]],
        #     # "format": "mp3", "split": "conversation", "channels": 2
        # },
        {
            "action": "stream",
            "streamUrl": [
                "https://d227vfuz68nmz8.cloudfront.net/audio_files/test_smoke3_music-on-hold-ten.wav"
            ],
            "bargeIn": "false",
        },
    ]


def ncco_stream_if_beep_start(event):
    return [
        {
            "action": "notify",
            "payload": {
                "event": "beep_start",
                "action": "stream",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        {
            "action": "record",
            "eventUrl": [event["notify_event_url"]],
            # commented out but will be useful to test extra parameters
            # "format": "mp3", "split": "conversation", "channels": 2
        },
        {
            "action": "stream",
            "streamUrl": [
                "https://d227vfuz68nmz8.cloudfront.net/audio_files/test_smoke3_music-on-hold-ten.wav"
            ],
            "bargeIn": "false",
            "loop": 1,
        },
    ]


def ncco_stream_if_beep_timeout(event):
    return [
        {
            "action": "notify",
            "payload": {
                "event": "beep_timeout",
                "action": "stream",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        {
            "action": "stream",
            "streamUrl": [
                "https://d227vfuz68nmz8.cloudfront.net/audio_files/test_smoke3_music-on-hold-ten.wav"
            ],
            "bargeIn": "false",
        },
    ]


#### NCCO Connect ####
def ncco_connect_if_human(event):
    destination_type = ""
    if event["type"] == "phone":
        destination_type = "number"
    elif event["type"] == "sip":
        destination_type = "uri"
    elif event["type"] == "vbc":
        destination_type = "extension"
    elif event["type"] == "websocket":
        destination_type = "uri"
    return [
        {
            "action": "notify",
            "payload": {
                "event": "human",
                "action": "connect",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        # commented out but will be useful to test parallel recording
        #     {
        #     "action": "record",
        #     "eventUrl": [event["notify_event_url"]],
        #     # "format": "mp3", "split": "conversation", "channels": 2
        # },
        {
            "action": "connect",
            "eventUrl": [event["notify_event_url"]],
            "limit": "5",
            "from": event["from"],
            "endpoint": [{"type": event["type"], destination_type: event["human"]}]
            if event["type"] != "websocket"
            else [
                {
                    "type": event["type"],
                    destination_type: event["human"],
                    "content-type": "audio/l16;rate=16000",
                }
            ],
        },
    ]


def ncco_connect_if_machine(event):
    destination_type = ""
    if event["type"] == "phone":
        destination_type = "number"
    elif event["type"] == "sip":
        destination_type = "uri"
    elif event["type"] == "vbc":
        destination_type = "extension"
    elif event["type"] == "websocket":
        destination_type = "uri"
    return [
        {
            "action": "notify",
            "payload": {
                "event": "machine",
                "action": "connect",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        # commented out but will be useful to test parallel recording
        #     {
        #     "action": "record",
        #     "eventUrl": [event["notify_event_url"]],
        #     # "format": "mp3", "split": "conversation", "channels": 2
        # },
        {
            "action": "connect",
            "eventUrl": [event["notify_event_url"]],
            "limit": "60",
            "endpoint": [{"type": event["type"], destination_type: event["machine"]}]
            if event["type"] != "websocket"
            else [
                {
                    "type": event["type"],
                    destination_type: event["machine"],
                    "content-type": "audio/l16;rate=16000",
                }
            ],
        },
    ]


def ncco_connect_if_beep_start(event):
    destination_type = ""
    if event["type"] == "phone":
        destination_type = "number"
    elif event["type"] == "sip":
        destination_type = "uri"
    elif event["type"] == "vbc":
        destination_type = "extension"
    elif event["type"] == "websocket":
        destination_type = "uri"
    return [
        {
            "action": "notify",
            "payload": {
                "event": "beep_start",
                "action": "connect",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        # commented out but will be useful to test parallel recording
        # {
        #     "action": "record",
        #     "eventUrl": [event["notify_event_url"]],
        #     # "format": "mp3", "split": "conversation", "channels": 2
        # },
        {
            "action": "connect",
            "eventUrl": [event["notify_event_url"]],
            "limit": "60",
            "endpoint": [{"type": event["type"], destination_type: event["beep_start"]}]
            if event["type"] != "websocket"
            else [
                {
                    "type": event["type"],
                    destination_type: event["beep_start"],
                    "content-type": "audio/l16;rate=16000",
                }
            ],
        },
    ]


def ncco_connect_if_beep_timeout(event):
    destination_type = ""
    if event["type"] == "phone":
        destination_type = "number"
    elif event["type"] == "sip":
        destination_type = "uri"
    elif event["type"] == "vbc":
        destination_type = "extension"
    elif event["type"] == "websocket":
        destination_type = "uri"
    return [
        {
            "action": "notify",
            "payload": {
                "event": "beep_timeout",
                "action": "connect",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        # commented out but will be useful to test parallel recording
        #     {
        #     "action": "record",
        #     "eventUrl": [event["notify_event_url"]],
        #     # "format": "mp3", "split": "conversation", "channels": 2
        # },
        {
            "action": "connect",
            "eventUrl": [event["notify_event_url"]],
            "limit": "10",
            "endpoint": [
                {"type": event["type"], destination_type: event["beep_timeout"]}
            ]
            if event["type"] != "websocket"
            else [
                {
                    "type": event["type"],
                    destination_type: event["beep_timeout"],
                    "content-type": "audio/l16;rate=16000",
                }
            ],
        },
    ]


#### NCCO Record ####
def ncco_record_if_human(event):
    destination_type = ""
    if event["type"] == "phone":
        destination_type = "number"
    elif event["type"] == "sip":
        destination_type = "uri"
    elif event["type"] == "vbc":
        destination_type = "extension"
    return [
        {
            "action": "notify",
            "payload": {
                "event": "human",
                "action": "record",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        {
            "action": "record",
            "eventUrl": [event["notify_event_url"]],
            # commented out but will be useful to test extra parameters
            # "format": "mp3", "split": "conversation", "channels": 2
        },
        # commented out but will be useful to test record + connect
        # {
        #     "action": "connect",
        #     "eventUrl": [event["notify_event_url"]],
        #     "limit": "20",
        #     "from": event["from"],
        #     "endpoint": [
        #         {"type": event["type"], destination_type: event["human"]}
        #     ],  # french speaker
        # },
    ]


def ncco_record_if_machine(event):
    destination_type = ""
    if event["type"] == "phone":
        destination_type = "number"
    elif event["type"] == "sip":
        destination_type = "uri"
    elif event["type"] == "vbc":
        destination_type = "extension"
    return [
        {
            "action": "notify",
            "payload": {
                "event": "machine",
                "action": "record",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        {
            "action": "record",
            "eventUrl": [event["notify_event_url"]],
            # commented out but will be useful to test extra parameters
            # "format": "mp3", "split": "conversation", "channels": 2
        },
        # commented out but will be useful to test record + connect
        # {
        #     "action": "connect",
        #     "eventUrl": [event["notify_event_url"]],
        #     "limit": "60",
        #     "endpoint": [
        #         {"type": event["type"], destination_type: event["machine"]}
        #     ],  # counts to 20
        # },
    ]


def ncco_record_if_beep_start(event):
    destination_type = ""
    if event["type"] == "phone":
        destination_type = "number"
    elif event["type"] == "sip":
        destination_type = "uri"
    elif event["type"] == "vbc":
        destination_type = "extension"
    return [
        {
            "action": "notify",
            "payload": {
                "event": "beep_start",
                "action": "record",
                "xuuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "xconversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        {
            "action": "record",
            "eventUrl": [event["notify_event_url"]],
            # commented out but will be useful to test extra parameters
            # "format": "mp3", "split": "conversation", "channels": 2
        },
        # commented out but will be useful to test parallel recording
        # {
        #     "action": "connect",
        #     "eventUrl": [event["notify_event_url"]],
        #     "limit": "20",
        #     "endpoint": [
        #         {"type": event["type"], destination_type: event["beep_start"]}
        #     ],  # music 15 seconds
        # },
    ]


def ncco_record_if_beep_timeout(event):
    destination_type = ""
    if event["type"] == "phone":
        destination_type = "number"
    elif event["type"] == "sip":
        destination_type = "uri"
    elif event["type"] == "vbc":
        destination_type = "extension"
    return [
        {
            "action": "notify",
            "payload": {
                "event": "beep_timeout",
                "action": "record",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        {
            "action": "record",
            "eventUrl": [event["notify_event_url"]],
            # commented out but will be useful to test extra parameters
            # "format": "mp3", "split": "conversation", "channels": 2
        },
        # commented out but will be useful to test parallel recording
        # {
        #     "action": "connect",
        #     "eventUrl": [event["notify_event_url"]],
        #     "limit": "20",
        #     "endpoint": [
        #         {"type": event["type"], destination_type: event["beep_timeout"]}
        #     ],  # chinese speaker
        # },
    ]


#### NCCO Conversation ####
def ncco_conversation_if_human(event):
    return [
        {
            "action": "notify",
            "payload": {
                "event": "human",
                "action": "conversation",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        {
            "action": "conversation",
            "muted": False,
            "record": True,
            "name": "{0}-hu".format(event["conversation_name"]),
            "earmuff": False,
            "playExitSound": True,
            "playEnterSound": True,
            "endOnExit": True,
            "startOnEnter": True,
            "conversationsTtl": 1,
            "eventCallbackUrl": [
                "{0}?qa_unique_id={1}&qa_type=recording".format(
                    event["notify_event_url"], event["conversation_name"]
                )
            ],
            "eventCallbackMethod": "GET",
        },
    ]


def ncco_conversation_if_machine(event):
    return [
        {
            "action": "notify",
            "payload": {
                "event": "machine",
                "action": "conversation",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        # commented out but will be useful to test parallel recording
        # {
        #     "action": "record",
        #     "eventUrl": [event["notify_event_url"]],
        #     # "format": "mp3", "split": "conversation", "channels": 2
        # },
        {
            "action": "conversation",
            "muted": False,
            "record": True,
            "name": "{0}-ma".format(event["conversation_name"]),
            "earmuff": False,
            "playExitSound": True,
            "playEnterSound": True,
            "endOnExit": True,
            "startOnEnter": True,
            "conversationsTtl": 1,
            "eventCallbackUrl": [event["notify_event_url"]],
            "eventCallbackMethod": "GET",
        },
    ]


def ncco_conversation_if_beep_start(event):
    return [
        {
            "action": "notify",
            "payload": {
                "event": "beep_start",
                "action": "conversation",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        {
            "action": "record",
            "eventUrl": [event["notify_event_url"]],
            # commented out but will be useful to test extra parameters
            # "format": "mp3", "split": "conversation", "channels": 2
        },
        {
            "action": "conversation",
            "muted": False,
            "record": True,
            "name": "{0}-ba".format(event["conversation_name"]),
            "earmuff": False,
            "playExitSound": True,
            "playEnterSound": True,
            "endOnExit": True,
            "startOnEnter": True,
            "conversationsTtl": 1,
            "eventCallbackUrl": [event["notify_event_url"]],
            "eventCallbackMethod": "GET",
        },
    ]


def ncco_conversation_if_beep_timeout(event):
    return [
        {
            "action": "notify",
            "payload": {
                "event": "beep_timeout",
                "action": "conversation",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        {
            "action": "conversation",
            "muted": False,
            "record": True,
            "name": "{0}-bt".format(event["conversation_name"]),
            "earmuff": False,
            "playExitSound": True,
            "playEnterSound": True,
            "endOnExit": True,
            "startOnEnter": True,
            "conversationsTtl": 1,
            "eventCallbackUrl": [event["notify_event_url"]],
            "eventCallbackMethod": "GET",
        },
    ]


#### NCCO Input ####
def ncco_input_if_human(event):
    return [
        {
            "action": "notify",
            "payload": {
                "event": "human",
                "action": "input",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        # commented out but will be useful to test parallel recording
        #   {
        #     "action": "record",
        #     "eventUrl": [event["notify_event_url"]],
        #     # "format": "mp3", "split": "conversation", "channels": 2
        # },
        {
            "action": "talk",
            "level": "1",
            "text": "You are now identified as human. Press 1 for stream action. Press 2 to record and connect action. Press 3 for conversation action.",
            "voiceName": "Amy",
        },
        {
            "action": "input",
            "type": ["dtmf"],
            "timeOut": "10",
            "eventUrl": [
                "{0}/dtmf?notify_event_url={1}".format(
                    event["SERVER_URL"], event["notify_event_url"]
                )
            ],
            "eventMethod": "POST",
        },
    ]


#### NCCO Notify ####
def ncco_notify_if_human(event):
    return [
        {
            "action": "notify",
            "payload": {
                "event": "human",
                "action": "notify",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
    ]


def ncco_notify_if_machine(event):
    return [
        # commented out but will be useful to test parallel recording
        #     {
        #     "action": "record",
        #     "eventUrl": [event["notify_event_url"]],
        #     # "format": "mp3", "split": "conversation", "channels": 2
        # },
        {
            "action": "notify",
            "payload": {
                "event": "machine",
                "action": "notify",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
    ]


def ncco_notify_if_beep_start(event):
    return [
        # commented out but will be useful to test parallel recording
        #       {
        #     "action": "record",
        #     "eventUrl": [event["notify_event_url"]],
        #     # "format": "mp3", "split": "conversation", "channels": 2
        # },
        {
            "action": "notify",
            "payload": {
                "event": "beep_start",
                "action": "notify",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
    ]


def ncco_notify_if_beep_timeout(event):
    return [
        {
            "action": "notify",
            "payload": {
                "event": "beep_timeout",
                "action": "notify",
                "uuid": event["uuid"] if "uuid" in event else event["call_uuid"],
                "conversation_uuid": event["conversation_uuid"],
            },
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
    ]


#### NCCO Answer URL for Application ####
def ncco_talkconnect_if_agent(event):
    destination_type = ""
    if event["type"] == "phone":
        destination_type = "number"
    elif event["type"] == "sip":
        destination_type = "uri"
    elif event["type"] == "vbc":
        destination_type = "extension"
    elif event["type"] == "websocket":
        destination_type = "uri"
    return [
        {"action": "record", "eventUrl": [event["notify_event_url"]]},
        {
            "action": "talk",
            "text": "Please wait while we connect you to the dialed number.",
            "language": "it-IT",
            "style": "4",
            "level": 1,
            "loop": 1,
        },
        {
            "action": "connect",
            "advancedMachineDetection": {
                "beep_timeout": "45",
                "mode": "default",
                "behavior": "continue",
            },
            "eventUrl": [
                "{0}/amd_event_url?action=talkconnect&type=phone&human=441174960039&machine=441234000002&beep_start=441174960012&beep_timeout=15555555555&notify_event_url={1}".format(
                    event["SERVER_URL"], event["notify_event_url"]
                )
            ],
            "from": event["from"],
            # "limit": "60",
            "endpoint": [
                {"type": event["type"], destination_type: event["destination"]}
            ]
            if event["type"] != "websocket"
            else [
                {
                    "type": event["type"],
                    destination_type: event["destination"],
                    "content-type": "audio/l16;rate=16000",
                }
            ],
        },
        {
            "action": "notify",
            "payload": {"event": "agent", "action": "talkconnect"},
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
    ]


def ncco_talkconnect_if_human(event):
    return [
        # commented out but will be useful to test parallel recording
        #   {
        #   "action": "record",
        #   "eventUrl": [event["notify_event_url"]]
        # },
        {
            "action": "talk",
            "text": "We are leaving this message to human. Please contact us immediately.",
            "language": "it-IT",
            "style": "4",
            "level": 1,
            "loop": 2,
        },
        # commented out but will be useful to test talk and connect
        # {
        #   "action":
        #   "connect",
        #   "eventUrl": [event["notify_event_url"]],
        #   "limit":
        #   "20",
        #   "endpoint": [{
        #     "type": "phone",
        #     "number": "15555555555"
        #   }]},
        #   {
        #   "action":
        #   "stream",
        #   "streamUrl": [
        #     "https://d227vfuz68nmz8.cloudfront.net/audio_files/test_smoke3_music-on-hold-ten.wav"
        #   ],
        #   "bargeIn": "false"
        # },
        {
            "action": "notify",
            "payload": {"event": "human", "action": "talkconnect"},
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
    ]


def ncco_talkconnect_if_machine(event):
    return [
        # commented out but will be useful to test parallel recording
        #   {
        #   "action": "record",
        #   "eventUrl": [event["notify_event_url"]]
        # },
        {
            "action": "notify",
            "payload": {"event": "machine", "action": "talkconnect"},
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
        {
            "action": "talk",
            "text": "We are leaving this message before the beep. Please contact us immediately.",
            "language": "it-IT",
            "style": "4",
            "level": 1,
            "loop": 2,
        },
        # commented out but will be useful to test talk and connect
        # {
        #   "action":
        #   "connect",
        #   "eventUrl": [event["notify_event_url"]],
        #   "limit":
        #   "20",
        #   "endpoint": [{
        #     "type": "phone",
        #     "number": "15555555555"
        #   }]},
        #   {
        #   "action":
        #   "stream",
        #   "streamUrl": [
        #     "https://d227vfuz68nmz8.cloudfront.net/audio_files/test_smoke3_music-on-hold-ten.wav"
        #   ],
        #   "bargeIn": "false"
        # },
    ]


def ncco_talkconnect_if_beep_start(event):
    return [
        # commented out but will be useful to test parallel recording
        #   {
        #   "action": "record",
        #   "eventUrl": [event["notify_event_url"]]
        # },
        {
            "action": "talk",
            "text": "We are leaving this message in your voicemail. Please contact us immediately.",
            "language": "it-IT",
            "style": "4",
            "level": 1,
            "loop": 2,
        },
        # commented out but will be useful to test talk and connect
        # {
        #   "action":
        #   "connect",
        #   "eventUrl": [event["notify_event_url"]],
        #   "limit":
        #   "20",
        #   "endpoint": [{
        #     "type": "phone",
        #     "number": "15555555555"
        #   }]},
        #   {
        #   "action":
        #   "stream",
        #   "streamUrl": [
        #     "https://d227vfuz68nmz8.cloudfront.net/audio_files/test_smoke3_music-on-hold-ten.wav"
        #   ],
        #   "bargeIn": "false"
        # },
        {
            "action": "notify",
            "payload": {"event": "beep_start", "action": "talkconnect"},
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
    ]


def ncco_talkconnect_if_beep_timeout(event):
    return [
        # commented out but will be useful to test parallel recording
        #   {
        #   "action": "record",
        #   "eventUrl": [event["notify_event_url"]]
        # },
        {
            "action": "talk",
            "text": "We are leaving this message after beep timeout. Please contact us immediately.",
            "language": "it-IT",
            "style": "4",
            "level": 1,
            "loop": 2,
        },
        # commented out but will be useful to test talk and conenct
        # {
        #   "action":
        #   "connect",
        #   "eventUrl": [event["notify_event_url"]],
        #   "limit":
        #   "20",
        #   "endpoint": [{
        #     "type": "phone",
        #     "number": "15555555555"
        #   }]},
        #   {
        #   "action":
        #   "stream",
        #   "streamUrl": [
        #     "https://d227vfuz68nmz8.cloudfront.net/audio_files/test_smoke3_music-on-hold-ten.wav"
        #   ],
        #   "bargeIn": "false"
        # },
        {
            "action": "notify",
            "payload": {"event": "beep_timeout", "action": "talkconnect"},
            "eventUrl": [event["notify_event_url"]],
            "eventMethod": "POST",
        },
    ]

### tts_01 ###
def tts_01_if_human(event):
    return [
        {
            "action": "talk",
            "voiceName": "Amy",
            "text": "I am talking to a human.",
            "level": 1,
            "loop": 3,
        },
    ]


def tts_01_if_machine(event):
    return [
        {
            "action": "talk",
            "voiceName": "Amy",
            "text": "I am talking to a machine before the beep.",
            "level": 1,
            "loop": 3,
        },
    ]

def tts_01_if_beep_start(event):
    return [
        {
            "action": "talk",
            "voiceName": "Amy",
            "text": "I am talking to voicemail after the beep.",
            "level": 1,
            "loop": 3,
        },
    ]

### connect_02 ###
def connect_02_if_human(event):
    destination_type = ""
    if event["type"] == "phone":
        destination_type = "number"
    elif event["type"] == "sip":
        destination_type = "uri"
    elif event["type"] == "vbc":
        destination_type = "extension"
    elif event["type"] == "websocket":
        destination_type = "uri"
    return [
        {
            "action": "connect",
            "eventUrl": [event["notify_event_url"]],
            "limit": "60",
            "from": event["from"],
            "endpoint": [{"type": event["type"], destination_type: event["destination"]}]
            if event["type"] != "websocket"
            else [
                {
                    "type": event["type"],
                    destination_type: event["destination"],
                    "content-type": "audio/l16;rate=16000",
                }
            ],
        },
    ]


def connect_02_if_machine(event):
    return [
        {
            "action": "talk",
            "voiceName": "Amy",
            "text": "I am talking to machine before the beep.",
            "level": 1,
            "loop": 3,
        },
    ]


def connect_02_if_beep_start(event):
    return [
        {
            "action": "talk",
            "voiceName": "Amy",
            "text": "I am talking to voicemail after the beep.",
            "level": 1,
            "loop": 3,
        },
    ]

#### named_conv_04 ####
def named_conv_04_if_human(event):
    return [
        {
            "action": "conversation",
            "muted": False,
            "record": False,
            "name": event["conversation_name"],
            "earmuff": False,
            "playExitSound": True,
            "playEnterSound": True,
            "endOnExit": True,
            "startOnEnter": False,
            "musicOnHoldUrl": ["https://static.dev.nexmoinc.net/svc/ncco/audio_files/wav/sample-8000_bitrate-16_channels-1_duration-225s.wav"],
            "conversationsTtl": 1,
            "eventCallbackUrl": [
                "{0}?qa_unique_id={1}".format(
                    event["notify_event_url"], event["conversation_name"]
                )
            ],
            "eventCallbackMethod": "GET",
        },
    ]


ncco_set = {
    "tts_01": {
        "human": tts_01_if_human,
        "machine": tts_01_if_machine,
        "beep_start": tts_01_if_beep_start,
    },
    "connect_02": {
        "human": connect_02_if_human,
        "machine": connect_02_if_machine,
        "beep_start": connect_02_if_beep_start,
    },
    "named_conv_04": {
        "human": named_conv_04_if_human,
    },
    "talk": {
        "machine": ncco_talk_if_machine,
        "human": ncco_talk_if_human,
        "beep_start": ncco_talk_if_beep_start,
        "fax": ncco_talk_if_fax,
        "beep_timeout": ncco_talk_if_beep_timeout,
    },
    "stream": {
        "machine": ncco_stream_if_machine,
        "human": ncco_stream_if_human,
        "beep_start": ncco_stream_if_beep_start,
        "beep_timeout": ncco_stream_if_beep_timeout,
    },
    "connect": {
        "machine": ncco_connect_if_machine,
        "human": ncco_connect_if_human,
        "beep_start": ncco_connect_if_beep_start,
        "beep_timeout": ncco_connect_if_beep_timeout,
    },
    "notify": {
        "machine": ncco_notify_if_machine,
        "human": ncco_notify_if_human,
        "beep_start": ncco_notify_if_beep_start,
        "beep_timeout": ncco_notify_if_beep_timeout,
    },
    "record": {
        "machine": ncco_record_if_machine,
        "human": ncco_record_if_human,
        "beep_start": ncco_record_if_beep_start,
        "beep_timeout": ncco_record_if_beep_timeout,
    },
    "conversation": {
        "machine": ncco_conversation_if_machine,
        "human": ncco_conversation_if_human,
        "beep_start": ncco_conversation_if_beep_start,
        "beep_timeout": ncco_conversation_if_beep_timeout,
    },
    "input": {"human": ncco_input_if_human},
    "talkconnect": {
        "agent": ncco_talkconnect_if_agent,
        "human": ncco_talkconnect_if_human,
        "machine": ncco_talkconnect_if_machine,
        "beep_start": ncco_talkconnect_if_beep_start,
        "beep_timeout": ncco_talkconnect_if_beep_timeout,
    },
}
