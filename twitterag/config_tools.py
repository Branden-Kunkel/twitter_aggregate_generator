# Twitter-AG configuration file. See docs before editing!

class ctools:

        """configuration tools"""


        authorization = {
                                
                                "bearer_token" : None, # string
                                "api_key" : None, # string
                                "api_secret_key" : None, # string
                        }


        tweet_lookup_params =   {
                                        "read_from_file?" : False, # bool

                                        "tweet_id" : None, # string

                                        "request_params" :      {
                                                                       "expansions" : "attachments.poll_ids,attachments.media_keys,author_id,edit_history_tweet_ids,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id", # string
                                                                        "media.fields" : "duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics,non_public_metrics,organic_metrics,promoted_metrics,alt_text,variants", # string
                                                                        "place.fields" : "contained_within,country,country_code,full_name,geo,id,name,place_type", # string
                                                                        "poll.fields" : "duration_minutes,end_datetime,id,options,voting_status", # string
                                                                        "tweet.fields" : "attachments,author_id,context_annotations,conversation_id,created_at,edit_controls,entities,geo,id,in_reply_to_user_id,lang,public_metrics,possibly_sensitive,referenced_tweets,reply_settings,source,text,withheld", # string 
                                                                }
                                }


        tweet_timeline_params = {

                                        "read_from_file?" : False, # bool

                                        "user_id" : None, # string

                                        "pagination" :  {
                                                                "paginate?" : False, # bool
                                                                "page_count" : 2 # int
                                                        },

                                        "request_params" :      {    
                                                                        "expansions" : "attachments.poll_ids,attachments.media_keys,author_id,edit_history_tweet_ids,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id", # string
                                                                        "max_results" : "5", # string
                                                                        "media.fields" : "duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics,non_public_metrics,organic_metrics,promoted_metrics,alt_text,variants", # string
                                                                        "place.fields" : "contained_within,country,country_code,full_name,geo,id,name,place_type", # string
                                                                        "poll.fields" : "duration_minutes,end_datetime,id,options,voting_status", # string
                                                                        "tweet.fields" : "attachments,author_id,context_annotations,conversation_id,created_at,edit_controls,entities,geo,id,in_reply_to_user_id,lang,public_metrics,possibly_sensitive,referenced_tweets,reply_settings,source,text,withheld", # string
                                                                        "pagination_token" : None, # string
                                                                        "exclude" : None, # string
                                                                        "start_time" : None, # string
                                                                        "end_time" : None, # string
                                                                        "until_id" : None, # string
                                                                },
                                }       


        user_profile_params =   {       
                                        "usernames" : None, # string

                                        "user_id" : None, # string

                                        "search_by_username?": True, # bool

                                        "request_params" :      {
                                                                        "user.fields" : "description,id,public_metrics,created_at,entities,location,name,profile_image_url,protected,url,username,verified,withheld", # string
                                                                        "expansions" : "pinned_tweet_id", # string
                                                                },

                                        "read_from_file?" : False, # bool               
                                }


        user_follows_params =   {
                                        "read_from_file?" : False, # bool

                                        "user_id" : None, # bool

                                        "request_params" :      {
                                                                        "user.fields" : "description,id,public_metrics,created_at,entities,location,name,profile_image_url,protected,url,username,verified,withheld", # string
                                                                        "expansions" : "pinned_tweet_id", # string
                                                                        "max_results" : "5", # string
                                                                        "pagination_token" : None # string
                                                                },

                                        "pagination" :  {
                                                                "paginate?" : False, # bool
                                                                "page_count" : 2 # int
                                                        }
                                        
                                }


        likes_params =  {
                                "read_from_file?": False, # bool

                                "tweet_id" : None, # string

                                "user_id" : None, # string

                                "pagination" :  {
                                                        "paginate?" : False, # bool
                                                        "page_count" : 2, # int
                                                },

                                "liking_request_params" :       {
                                                                        "user.fields" : "description,id,public_metrics,created_at,entities,location,name,profile_image_url,protected,url,username,verified,withheld", # string
                                                                        "expansions" : "pinned_tweet_id", # string
                                                                        "max_results" : "5", # string
                                                                        "pagination_token" : None # string
                                                                },

                                "liked_request_params" :        {    
                                                                        "expansions" : "attachments.poll_ids,attachments.media_keys,author_id,edit_history_tweet_ids,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id", # string
                                                                        "max_results" : "5", # string
                                                                        "media.fields" : "duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics,non_public_metrics,organic_metrics,promoted_metrics,alt_text,variants", # string
                                                                        "place.fields" : "contained_within,country,country_code,full_name,geo,id,name,place_type", # string
                                                                        "poll.fields" : "duration_minutes,end_datetime,id,options,voting_status", # string
                                                                        "tweet.fields" : "attachments,author_id,context_annotations,conversation_id,created_at,edit_controls,entities,geo,id,in_reply_to_user_id,lang,public_metrics,possibly_sensitive,referenced_tweets,reply_settings,source,text,withheld", # string
                                                                        "pagination_token" : None, # string
                                                                        "exclude" : None, # string
                                                                        "start_time" : None, # string
                                                                        "end_time" : None, # string
                                                                        "until_id" : None, # string
                                                                },
                        }


        GLOBAL_FILE_PATH = "" # string


        file_IO =       {
                                "out" : {

                                                "user_profile" :        {
                                                                                "user_profiles" : GLOBAL_FILE_PATH + "", # string
                                                                        },

                                                "tweet_timeline" :      {
                                                                                "tweet_timelines" : GLOBAL_FILE_PATH + "", # string
                                                                        },

                                                "user_follows" :        {
                                                                                "user_followers" : GLOBAL_FILE_PATH + "", # string

                                                                                "user_following" : GLOBAL_FILE_PATH + "", # string
                                                                        },

                                                "tweet_lookup" :        {
                                                                                "tweets" : GLOBAL_FILE_PATH + "", # string
                                                                        },

                                                "likes" :               {
                                                                                "liking" : GLOBAL_FILE_PATH + "", # string

                                                                                "liked" : GLOBAL_FILE_PATH + "", # string
                                                                        },
                                                
                                        },


                                "in" :  {
                                                "user_profile" :        {
                                                                                "username_list" : GLOBAL_FILE_PATH + "", # string

                                                                                "user_id_list" : GLOBAL_FILE_PATH + "", # string
                                                                        },

                                                "tweet_timeline" :      {
                                                                                "user_id_list" : GLOBAL_FILE_PATH + "", # string
                                                                        },

                                                "user_follows" :        {
                                                                                "user_id_list" : GLOBAL_FILE_PATH + "", # string
                                                                        },

                                                "tweet_lookup" :        {
                                                                                "tweet_id_list" : GLOBAL_FILE_PATH + "" # string
                                                                        },

                                                "likes" :               {
                                                                                "user_id_list" : GLOBAL_FILE_PATH + "", # string

                                                                                "tweet_id_list" : GLOBAL_FILE_PATH + "", # string
                                                                        },      
                                        }
                        }


        genopts =       {
                                "verbose?" : True # bool
                        }

