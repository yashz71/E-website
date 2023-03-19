from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock

class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required=False,
        help_text="Title to display",
    )
    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = "Title"
        help_text = "Centered text to be displayed on the page"

class LinkValue(blocks.StructValue):
    def url(self) -> str:
        internal_page = self.get("internal_page")
        external_link = self.get("external_link")
        if internal_page:
            return internal_page.url
        elif external_link:
            return external_link
        else:
            return ""

class Link(blocks.StructBlock):
    link_text = blocks.CharBlock(
        max_length=50,
        default="more details"
    )
    internal_page = blocks.PageChooserBlock(
        required=False
    )
    external_link = blocks.URLBlock(
        required=False
    )
    class Meta:
        value_class = LinkValue

class Card(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=140,
        help_text="Bold title text for this card max length is 140"
     )
    text = blocks.TextBlock(
        max_length=250,
        help_text="optianol text for this card max length 250",
        required=False
    )
    image = ImageChooserBlock(
        required=False,
        help_text="thsi image will be cropped"
    )
    link = Link()




class CardBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        Card()
    )
    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "standard cards"


class ImagesAndTextBlock(blocks.StructBlock):
    image = ImageChooserBlock(help_text="this image will be cropped")
    image_alignement = blocks.ChoiceBlock(
        choices=(
        ("left", "Left"),
        ("right", "Right"),
        ("center", "Center")
    ),
        help_text="image on left and text on right o image on the right and text on the left"
    )
    title = blocks.CharBlock(max_length=50, help_text="max charachters is 50")
    text = blocks.CharBlock(required=False, max_length=140)
    link = Link()
    class Meta:
        template = "streams/images_and_textblock.html"
        icon ="image"
        label="image & text"

class CallToAction(blocks.StructBlock):
    title = blocks.CharBlock(max_length=200, help_text="the max length is 200 charachters")
    link = Link()
    class Meta:
        template = "streams/call_to_action.html"
        icon = "plus"
        label = "Call To Action"

class PricingTableBlock(TableBlock):

    class Meta:
        template = "streams/pricing_table_block.html"
        icon = "table"
        label = "Pricing Table"
