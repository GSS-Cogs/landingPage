document.addEventListener('DOMContentLoaded', function() {
    chrome.tabs.getSelected(null, (tabInfo) => {
        fetch('https://cogs.floop.org.uk/?landingPage=' + encodeURI(tabInfo.url))
            .then((response) => response.text())
            .then((html) => {
                document.getElementById('body').innerHTML = html;
            });
    });
}, false);
