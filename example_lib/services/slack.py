from slacker import Slacker

class Slack:

    def __init__(self):
        self.token = SLACK_TOKEN
        self.channel = SLACK_CHANNEL
        self.icon = SLACK_ICON
        self.username = SLACK_USERNAME

    def find_color(self, type:str) -> str:
        """ Finds the color that corresponds to the type
        of the message.

        Args:
            type (str): Type of the message, either : success,
            info, warning, error.

        Returns:
            str : Returns the hex color code for the Slack message. 
        """
        if type == "success":
            return "#47D861"
        elif type == "info":
            return "#2F86E7"
        elif type == "warning":
            return "#FFBF24"
        elif type == "error":
            return "#FE355B"
        return type

    def create_message(self, title:str,  message:str, type:str) -> list:
        """ Creates the message attachments for the Slack message.
        Used for formatting the message and sets things like color.

        Args:
            title (str): Title in bold of the Slack message
            message (str): Message underneath the title.
            type (str): Type of the message either : success, info, warning, error 
            or even a custom hex color code. 

        Returns:
            list: Returns the attachment required to format the Slack message
        """
        return [{
            "title": title,
            "color": self.find_color(type),
            "text": message
        }]

    def send_slack(self, title:str, message:str, type:str=None) -> None:
        """ 
        Args:
            title (str): Title in bold of the Slack message
            message (str): Message underneath the title.
            type (str): Type of the message either : success, error, info, warning 
        """
        slack = Slack(self.token) 
        slack.chat.post_message(channel=self.channel,
                                attachments=self.create_message(title,message,type),
                                username=self.username,
                                icon_url=self.icon)