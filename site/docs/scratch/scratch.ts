const add_admin_user = (
    username: string,
    add_user_db: (username: string, is_admin: boolean) => boolean): boolean => {
    return add_user_db(username, true);
}