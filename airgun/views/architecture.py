from widgetastic.widget import View, Text, TextInput

from airgun.widgets import ResourceList, Search


class ArchitectureView(View):
    title = Text("//h1[text()='Architectures']")
    new = Text("//a[contains(@href, '/architectures/new')]")
    navigate_locator = "//a[@id='menu_item_architectures']"
    search_element = Search()

    @property
    def is_displayed(self):
        return self.browser.wait_for_element(
            self.title, exception=False) is not None


class ArchitectureDetailsView(View):
    name = TextInput(locator="//input[@id='architecture_name']")
    submit = Text('//input[@name="commit"]')
    os_element = ResourceList(
        parent_entity='Architect', affected_entity='OperatingSystem')

    @property
    def is_displayed(self):
        return self.browser.wait_for_element(
            self.name, exception=False) is not None

    def submit_data(self):
        self.browser.click(self.submit)