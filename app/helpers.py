
def dash_embeds(name: str):
    embeds = {
        'sales': """
                <iframe width="100%" height="850" 
                    src="https://lookerstudio.google.com/embed/reporting/e5b15a4d-41dd-418e-971b-5c406f5fdc1e/page/pSVnD"
                    frameborder="0" 
                    style="border:0" 
                    allowfullscreen 
                    andbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">
                </iframe>
            """,
        'webinar': """
                <iframe width="100%" height="850" 
                    src="https://lookerstudio.google.com/embed/reporting/06791da2-f938-400a-b87a-406597382885/page/XM0mD"
                    frameborder="0" 
                    style="border:0" 
                    allowfullscreen 
                    andbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">
                </iframe>
            """,
        'youtube_calls': """
                <iframe width="100%" height="850" 
                    src="https://lookerstudio.google.com/embed/reporting/57445007-3b4a-43b9-8e5e-83e78169b08d/page/XM0mD""
                    frameborder="0" 
                    style="border:0" 
                    allowfullscreen 
                    andbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">
                </iframe>
            """,
        'youtube_webinar': """
                <iframe width="100%" height="850" 
                    src="https://lookerstudio.google.com/embed/reporting/225e24db-59b8-41aa-8b3b-c5302cf29026/page/XM0mD"
                    frameborder="0" 
                    style="border:0" 
                    allowfullscreen 
                    andbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">
                </iframe>
            """,
        'instagram': """
                <iframe width="100%" height="850" 
                    src="https://lookerstudio.google.com/embed/reporting/509768e1-0d53-4991-8ed7-a68d653073ea/page/wGHpD"
                    frameborder="0" 
                    style="border:0" 
                    allowfullscreen 
                    andbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">
                </iframe>
            """,
        'emc_instagram': """
                <iframe width="100%" height="850" 
                    src="https://lookerstudio.google.com/embed/reporting/3d641a1b-6ad0-4e8b-89ca-5bc62b87affa/page/wGHpD"
                    frameborder="0" 
                    style="border:0" 
                    allowfullscreen 
                    andbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">
                </iframe>
            """,
        'facebook': """
                <iframe width="100%" height="850" 
                    src="https://lookerstudio.google.com/embed/reporting/0e9d4de7-e4ff-4ab7-b1ef-7f98fcffb056/page/wGHpD"
                    frameborder="0" 
                    style="border:0" 
                    allowfullscreen 
                    andbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">
                </iframe>
            """,
    }
    return embeds.get(name)