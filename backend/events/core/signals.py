def event_removal_handler(sender, **kwargs):
    event = kwargs.get('instance')

    if event.event_background:
        # pass false so FileField doesn't save the model 
        event.event_background.delete(False)

    if event.event_banner:
        event.event_banner.delete(False)

    if event.event_partners:
        # erase relationship
        event.event_partners.clear()

    if event.event_pictures:
        # erase relationship
        event.event_pictures.clear()

        # TODO: erase pictures from disk
        # for picture in event.event_pictures.all():
        #     print(type(picture))
        #     print(picture)
        #     picture.delete(False)


def partner_removal_handler(sender, **kwargs):
    partner = kwargs.get('instance')

    if partner.partner_image:
        partner.partner_image.delete(False)


def picture_removal_handler(sender, **kwargs):
    picture = kwargs.get('instance')

    if picture.picture:
        picture.picture.delete(False)
