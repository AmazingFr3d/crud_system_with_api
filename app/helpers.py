
def iframe_const(url: str):
    return f"""
                <iframe width="100%" height="850" 
                    src="{url}"
                    frameborder="0" 
                    style="border:0" 
                    allowfullscreen 
                    andbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">
                </iframe>
            """

def dash_embeds(name: str):
    embeds = {
        'sales': iframe_const("https://lookerstudio.google.com/embed/reporting/e5b15a4d-41dd-418e-971b-5c406f5fdc1e/page/pSVnD"),
        'webinar': iframe_const("https://lookerstudio.google.com/embed/reporting/06791da2-f938-400a-b87a-406597382885/page/XM0mD"),
        'youtube_calls': iframe_const("https://lookerstudio.google.com/embed/reporting/57445007-3b4a-43b9-8e5e-83e78169b08d/page/XM0mD"),
        'youtube_webinar': iframe_const("https://lookerstudio.google.com/embed/reporting/225e24db-59b8-41aa-8b3b-c5302cf29026/page/XM0mD"),
        'instagram': iframe_const("https://lookerstudio.google.com/embed/reporting/509768e1-0d53-4991-8ed7-a68d653073ea/page/wGHpD"),
        'emc_instagram': iframe_const("https://lookerstudio.google.com/embed/reporting/3d641a1b-6ad0-4e8b-89ca-5bc62b87affa/page/wGHpD"),
        'facebook': iframe_const("https://lookerstudio.google.com/embed/reporting/0e9d4de7-e4ff-4ab7-b1ef-7f98fcffb056/page/wGHpD"),
        'twitter': iframe_const("https://lookerstudio.google.com/embed/reporting/ae474dce-63bd-4109-82b5-e28b3267881b/page/wGHpD"),
        'emc_twitter': iframe_const("https://lookerstudio.google.com/embed/reporting/c6b4ca5d-a527-43aa-9e9e-c7274c944c51/page/wGHpD"),
        'linkedin': iframe_const("https://lookerstudio.google.com/embed/reporting/0249b245-1afc-4c5b-a503-fc938bb57916/page/wGHpD"),
        'emc_linkedin': iframe_const("https://lookerstudio.google.com/embed/reporting/05b1a1f6-cdce-4511-8e1f-9173352e6d16/page/wGHpD"),
        'tiktok': iframe_const("https://lookerstudio.google.com/embed/reporting/9f45899f-ad3b-4427-8d25-cb155c972dbb/page/wGHpD"),
        'emc_tiktok': iframe_const("https://lookerstudio.google.com/embed/reporting/0bd7c906-e162-49b5-a2ea-8105a1ea11f0/page/wGHpD"),
        'youtube': iframe_const("https://lookerstudio.google.com/embed/reporting/4bc9eb18-89c5-4c97-94c3-9635f5b762ef/page/jdLp"),
        }
    return embeds.get(name)