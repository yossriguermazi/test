import logging
from pymongo import monitoring


class RequestsLogger(monitoring.CommandListener):
    def started(self, event):
        logging.warning(
            "Command {0.command_name} with request id "
            "{0.request_id} started on server "
            "{0.connection_id}".format(event)
        )

    def succeeded(self, event):
        logging.warning(
            "Command {0.command_name} with request id "
            "{0.request_id} on server {0.connection_id} "
            "succeeded in {0.duration_micros} "
            "microseconds".format(event)
        )

    def failed(self, event):
        logging.warning(
            "Command {0.command_name} with request id "
            "{0.request_id} on server {0.connection_id} "
            "failed in {0.duration_micros} "
            "microseconds".format(event)
        )


class ConnectionLogger(monitoring.ConnectionPoolListener):
    def pool_created(self, event):
        logging.warning("[pool {0.address}] pool created successfully".format(event))

    def pool_ready(self, event):
        logging.warning("[pool {0.address}] pool is ready to use".format(event))

    def pool_cleared(self, event): ...

    # logging.warning("[pool {0.address}] pool cleared".format(event))

    def pool_closed(self, event): ...

    # logging.warning("[pool {0.address}] pool closed".format(event))

    def connection_created(self, event):
        logging.warning(
            "[pool {0.address}][connection #{0.connection_id}] "
            "connection created".format(event)
        )

    def connection_ready(self, event):
        logging.warning(
            "[pool {0.address}][connection #{0.connection_id}] "
            "connection setup succeeded".format(event)
        )

    def connection_closed(self, event):
        logging.warning(
            "[pool {0.address}][connection #{0.connection_id}] "
            "connection closed, reason: "
            "{0.reason}".format(event)
        )

    def connection_check_out_started(self, event): ...

    # logging.warning("[pool {0.address}] connection check out " "started".format(event))

    def connection_check_out_failed(self, event): ...

    # logging.warning("[pool {0.address}] connection check out ""failed, reason: {0.reason}".format(event))

    def connection_checked_out(self, event): ...

    # logging.warning("[pool {0.address}][connection #{0.connection_id}] ""connection checked out of pool".format(event))

    def connection_checked_in(self, event): ...

    # logging.warning("[pool {0.address}][connection #{0.connection_id}] ""connection checked into pool".format(event))
