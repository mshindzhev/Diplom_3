from page_object.pages.base_page import BasePage


class FeedPage(BasePage):
    def count_orders(self, locator):
        current_counter = int(feed_page.get_text_to_element(locator))
        return current_counter == initial_counter + 1

