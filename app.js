const { LinkedinScraper, relevanceFilter, timeFilter, typeFilter, experienceLevelFilter, onSiteOrRemoteFilter, events } = require('linkedin-jobs-scraper');

(async () => {
    const scraper = new LinkedinScraper({
        headless: true,
        slowMo: 10,
    });

    // Log available events
    console.log(events);

    // Correctly use the event name for 'data'
    scraper.on(events.scraper.data, ({ query, location, link, title, company, place, description, date }) => {
        console.log(`${query} ${location} -> ${title} @ ${company} (${place}) [${date}]`);
        console.log(description);
        console.log(link);
    });

    await scraper.run([
        {
            query: 'Software Engineer',
            options: {
                locations: ['San Francisco'],
                filters: {
                    relevance: relevanceFilter.RELEVANT,
                    time: timeFilter.MONTH,
                    type: typeFilter.FULL_TIME,
                    experience: experienceLevelFilter.MID_SENIOR,
                    remote: onSiteOrRemoteFilter.REMOTE,
                }
            }
        }
    ]);

    await scraper.close();
})();
