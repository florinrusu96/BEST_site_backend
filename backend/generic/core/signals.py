def partner_removal_handler(sender, **kwargs):
    partner = kwargs.get('instance')

    if partner.image:
        # Pass false so FileField doesn't save the model.
        partner.image.delete(False)
    