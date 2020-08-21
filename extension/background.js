
// TODO - needs to be dynamic somehow or we'll keep having to updating this list
const urlPrefixes = [
    "https://www.gov.uk/",
    "https://gov.wales/",
    "https://api.beta.ons.gov.uk/",
    "https://www.ons.gov.uk/",
    "https://www.gov.uk/government/",
    "https://www.nrscotland.gov.uk/",
    "https://www.nisra.gov.uk/",
    "https://www.uktradeinfo.com/",
    "https://www.justice-ni.gov.uk/",
    "https://www.health-ni.gov.uk/",
    "http://www.isdscotland.org/",
    "https://digital.nhs.uk/",
    "https://statswales.gov.wales/",
    "https://www2.gov.scot/",
    "https://www.communities-ni.gov.uk/",
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