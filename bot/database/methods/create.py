from bot.database.methods.update import main_set_select, get_unique_code


def create_ref_url(main_name, description):
    # Создаёт реферальную ссылку
    main_set_select("invitation_links", main_name, description, 1, "")
