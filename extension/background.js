const urlPrefixes = [
    "https://www.gov.uk/government/",
    "https://gov.wales/",
    "https://api.beta.ons.gov.uk",
    "https://www.ons.gov.uk/",
    "https://www.gov.uk/government/",
    "https://www.nrscotland.gov.uk/statistics-and-data/statistics/",
    "https://www.nisra.gov.uk/publications/",
    "https://www.uktradeinfo.com/Statistics/Pages/",
    "https://www.uktradeinfo.com/Statistics/OverseasTradeStatistics/AboutOverseastradeStatistics/Pages/OTSReports.aspx",
    "https://www.uktradeinfo.com/Statistics/RTS/Pages/default.aspx",
    "https://www.justice-ni.gov.uk/publications/",
    "https://www.health-ni.gov.uk/publications/",
    "http://www.isdscotland.org/Health-Topics/",
    "https://digital.nhs.uk/data-and-information/publications/statistical/",
    "https://statswales.gov.wales/Catalogue",
    "https://www2.gov.scot/Topics/Statistics/Browse/",
    "https://www.communities-ni.gov.uk/publications/topic",
    "https://gov.wales/"
];

chrome.runtime.onInstalled.addListener(function () {
    chrome.declarativeContent.onPageChanged.removeRules(undefined, function () {
        chrome.declarativeContent.onPageChanged.addRules([
            {
                conditions: urlPrefixes.map((prefix) =>
                    new chrome.declarativeContent.PageStateMatcher({pageUrl: {urlPrefix: prefix}})
                ),
                actions: [new chrome.declarativeContent.ShowPageAction()]
            }
        ]);
    });
});
