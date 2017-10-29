from html import HTML
import configurations
import utility


def create_table_from_news_api_response(news_api_response):
    """Create a HTML table from the News API response"""
    if news_api_response is not None:
        ok_string = "ok"
        if news_api_response["status"] == ok_string:
            print "The API response is OK"
            all_articles = news_api_response["articles"]
            h = HTML()
            t = h.table(border='1')
            first_row = t.tr

            # Print the table headers
            for news_article_detail in configurations.new_article_details:
                first_row.th(news_article_detail)

            # Print the details in the table
            for article in all_articles:
                r = t.tr
                for news_article_detail in configurations.new_article_details:
                    r.td(article[news_article_detail])

            utility.write_text_to_file(str(t))
            utility.open_file_path_in_browser(configurations.output_file_location)