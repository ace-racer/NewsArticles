from html import HTML
import configurations
import utility
import random


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
                first_row.th(news_article_detail[0])

            # Print the details in the table
            for article in all_articles:
                r = t.tr
                for news_article_detail in configurations.new_article_details:
                    td = r.td
                    utility.create_html_element_based_on_details(article[news_article_detail[0]], news_article_detail[1], td)

            random_number = random.randint(1, 1000000001)
            file_name = utility.replace_placeholders_in_string(configurations.output_file_name, [str(random_number)])
            complete_file_location = configurations.output_file_location + file_name
            utility.write_text_to_file(str(h), complete_file_location)
            utility.open_file_path_in_browser(complete_file_location)