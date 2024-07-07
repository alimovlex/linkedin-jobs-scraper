#!/usr/bin/env python
import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData, EventMetrics
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters

# Configure logging
logging.basicConfig(level=logging.INFO)

# Event handlers
def on_data(data: EventData):
    print('[ON_DATA]', data.title, data.company, data.company_link, data.date, data.link, data.insights, data.description)

def on_metrics(metrics: EventMetrics):
    print('[ON_METRICS]', str(metrics))

def on_error(error):
    print('[ON_ERROR]', error)

def on_end():
    print('[ON_END]')

# Initialize the scraper
scraper = LinkedinScraper(
    chrome_executable_path=None,
    chrome_binary_location=None,
    chrome_options=None,
    headless=True,  # Set to False to see browser actions
    max_workers=1,
    slow_mo=1.3,
    page_load_timeout=10000
)

# Add event listeners
scraper.on(Events.DATA, on_data)
scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

# Define queries
queries = [
    Query(
        query='Software Engineer',
        options=QueryOptions(
            locations=['San Francisco'],
            apply_link=True,
            skip_promoted_jobs=True,
            page_offset=0,  # Start from the first page
            limit=999,
            filters=QueryFilters(
                #relevance=RelevanceFilters.RECENT,
                #time=TimeFilters.MONTH
            )
        )
    ),
]

# Run the scraper
scraper.run(queries)
