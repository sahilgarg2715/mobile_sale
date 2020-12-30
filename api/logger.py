import logging


class ContextFilter(logging.Filter):
    """
    This is a filter which injects contextual information into the log.
    """

    def filter(self, record):
        record_line = ""
        exception = ""
        request = ""
        module_event = ""
        response = ""
        users = ""
        additional_info = ""

        # Capture the exception if any
        if record.exc_info:
            exc_info1, exc_info2, exc_info3 = record.exc_info
            if exc_info1 or exc_info2 or exc_info3:
                exception = record.exc_info

        # Check if user has passed any args.
        if record.args:
            # Get module and event
            module = record.args.get("module")
            event = record.args.get("event")
            module_event = f" [MODULE: {module}, EVENT: {event}]"

            # Get request, this is newly added arg to log record
            request = record.args.get("request") or ""

            # get respose and errors
            if record.args.get("response"):
                response = "RESPONSE: {}, ".format(record.args.get("response"))
            if record.args.get("errors"):
                response = response + "ERROR: {}, ".format(record.args.get("errors"))

            # Fetch users detail
            if record.args.get("creator_user"):
                users = "CREATOR USER: {}".format(record.args.get("creator_user"))

            # Check for additional info
            additional_info = record.args.get("additional_info") or ""

        if users:
            users = f" [{users}]"

        if request:
            request = f" [REQUEST: {request}]"

        # combined exception with response
        if exception:
            response = response + f"EXCEPTION: {exception}"
        if response:
            response = f" [{response}]"

        if additional_info:
            additional_info = f" [ADDITIONAL INFO: {additional_info}]"

        record_line = (
            record_line + module_event + users + request + response + additional_info
        )
        record.record_line = record_line
        return True


class LogRecord:
    def __init__(self):
        pass

    def createRecord(
        self,
        module=None,
        event=None,
        creator_user=None,
        response=None,
        request=None,
        errors=None,
        additional_info=None,
    ):
        return {
            "module": module,
            "event": event,
            "creator_user": creator_user,
            "request": request,
            "response": response,
            "errors": errors,
            "additional_info": additional_info,
        }


logger = logging.getLogger("api")
f = ContextFilter()
logger.addFilter(f)
