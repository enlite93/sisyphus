import time
from .base_daemon import Daemon as BaseDaemon
import logging

class Daemon(BaseDaemon):

    def setup_logging(self):
        logging.basicConfig(filename='/tmp/sisyphus.log',level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

    def run(self):
        print "Running"
        self.setup_logging()
        try:
            while True:
                """
                Keep spawning new processes...
                
                Monitor the number of running processes
                
                If the number is smaller than the given bounds (either number of processes or percent of memory / CPU), spawn a new process using subprocess command
                """
                time.sleep(1)
                self.logger.info("Zzzzzz...")
        except SystemExit:
            self.logger("Exiting...")    
