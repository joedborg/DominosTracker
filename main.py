import urllib2
from xml.etree.ElementTree import fromstring


class DominosTracker(object):
    """

    """
    def __init__(self, session_id):
        """
        Get the session ID and then 
        form a URL to query.
        """
        self.url = "http://www.dominos.co.uk/checkout/pizzaTrackeriFrame.aspx?id=%s" % (session_id)

    def __call__(self):
        """
        Start tracking.
        """
        self.refresh()

    def refresh(self):
        """
        Reread the page and parse 
        the DOM.
        """
        self.dom = fromstring(urllib2.urlopen(self.url).read()).get("body").get("div")
        
