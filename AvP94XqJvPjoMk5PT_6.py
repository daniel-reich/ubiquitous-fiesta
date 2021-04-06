
unique_styles = lambda lst: len(set(style for styles in lst
                                    for style in styles.split(',')))

