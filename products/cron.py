import cronitor
import os
from dotenv import load_dotenv

load_dotenv()
cronitor.api_key = os.getenv("CRON_API_KEY")

cronitor.Monitor.put(
    key='test-cron',
    type='job',
    schedule='*/2 * * * *'
)


@cronitor.job('test-cron')
def test_cron():
    print('le test cron marche.')
