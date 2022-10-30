
class ctools:

        """configuration tools"""


        authorization = {
                                
                                "bearer_token" : None,
                                "api_key" : None,
                                "api_secret_key" : None
                        }


        tweet_lookup_params =   {
                                        "read_from_file?" : False,

                                        "tweet_id" : None,

                                        "request_params" :      {
                                                                       "expansions" : "attachments.poll_ids,attachments.media_keys,author_id,edit_history_tweet_ids,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id",
                                                                        "media.fields" : "duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics,non_public_metrics,organic_metrics,promoted_metrics,alt_text,variants",
                                                                        "place.fields" : "contained_within,country,country_code,full_name,geo,id,name,place_type",
                                                                        "poll.fields" : "duration_minutes,end_datetime,id,options,voting_status",
                                                                        "tweet.fields" : "attachments,author_id,context_annotations,conversation_id,created_at,edit_controls,entities,geo,id,in_reply_to_user_id,lang,public_metrics,possibly_sensitive,referenced_tweets,reply_settings,source,text,withheld", 
                                                                }
                                }


        tweet_timeline_params = {

                                        "read_from_file?" : False,

                                        "user_id" : None,

                                        "pagination" :  {
                                                                "paginate?" : False,
                                                                "page_count" : 2
                                                        },

                                        "request_params" :      {    
                                                                        "expansions" : "attachments.poll_ids,attachments.media_keys,author_id,edit_history_tweet_ids,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id",
                                                                        "max_results" : "5",
                                                                        "media.fields" : "duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics,non_public_metrics,organic_metrics,promoted_metrics,alt_text,variants",
                                                                        "place.fields" : "contained_within,country,country_code,full_name,geo,id,name,place_type",
                                                                        "poll.fields" : "duration_minutes,end_datetime,id,options,voting_status",
                                                                        "tweet.fields" : "attachments,author_id,context_annotations,conversation_id,created_at,edit_controls,entities,geo,id,in_reply_to_user_id,lang,public_metrics,possibly_sensitive,referenced_tweets,reply_settings,source,text,withheld",
                                                                        "pagination_token" : None,
                                                                        "exclude" : None,
                                                                        "start_time" : None,
                                                                        "end_time" : None,
                                                                        "until_id" : None,
                                                                },
                                }       


        user_profile_params =   {       
                                        "usernames" : None,

                                        "user_id" : None,

                                        "search_by_username?": True,

                                        "request_params" :      {
                                                                        "user.fields" : "description,id,public_metrics,created_at,entities,location,name,profile_image_url,protected,url,username,verified,withheld",
                                                                        "expansions" : "pinned_tweet_id",
                                                                },

                                        "read_from_file?" : False,               
                                }


        user_follows_params =   {
                                        "read_from_file?" : False,

                                        "user_id" : None,

                                        "request_params" :      {
                                                                        "user.fields" : "description,id,public_metrics,created_at,entities,location,name,profile_image_url,protected,url,username,verified,withheld",
                                                                        "expansions" : "pinned_tweet_id",
                                                                        "max_results" : "5",
                                                                        "pagination_token" : None
                                                                },

                                        "pagination" :  {
                                                                "paginate?" : False,
                                                                "page_count" : 2
                                                        }
                                        
                                }


        likes_params =  {
                                "read_from_file?": False,

                                "tweet_id" : None,

                                "user_id" : None,

                                "pagination" :  {
                                                        "paginate?" : False,
                                                        "page_count" : 2,
                                                },

                                "liking_request_params" :       {
                                                                        "user.fields" : "description,id,public_metrics,created_at,entities,location,name,profile_image_url,protected,url,username,verified,withheld",
                                                                        "expansions" : "pinned_tweet_id",
                                                                        "max_results" : "5",
                                                                        "pagination_token" : None
                                                                },

                                "liked_request_params" :        {    
                                                                        "expansions" : "attachments.poll_ids,attachments.media_keys,author_id,edit_history_tweet_ids,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id",
                                                                        "max_results" : "5",
                                                                        "media.fields" : "duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics,non_public_metrics,organic_metrics,promoted_metrics,alt_text,variants",
                                                                        "place.fields" : "contained_within,country,country_code,full_name,geo,id,name,place_type",
                                                                        "poll.fields" : "duration_minutes,end_datetime,id,options,voting_status",
                                                                        "tweet.fields" : "attachments,author_id,context_annotations,conversation_id,created_at,edit_controls,entities,geo,id,in_reply_to_user_id,lang,public_metrics,possibly_sensitive,referenced_tweets,reply_settings,source,text,withheld",
                                                                        "pagination_token" : None,
                                                                        "exclude" : None,
                                                                        "start_time" : None,
                                                                        "end_time" : None,
                                                                        "until_id" : None,
                                                                },
                        }


        GLOBAL_FILE_PATH = ""


        file_IO =       {
                                "out" : {

                                                "user_profile" :        {
                                                                                "user_profiles" : GLOBAL_FILE_PATH + "",
                                                                        },

                                                "tweet_timeline" :      {
                                                                                "tweet_timelines" : GLOBAL_FILE_PATH + "",
                                                                        },

                                                "user_follows" :        {
                                                                                "user_followers" : GLOBAL_FILE_PATH + "",

                                                                                "user_following" : GLOBAL_FILE_PATH + ""
                                                                        },

                                                "tweet_lookup" :        {
                                                                                "tweets" : GLOBAL_FILE_PATH + ""
                                                                        },

                                                "likes" :       {
                                                                        "liking" : GLOBAL_FILE_PATH + "",
                                                                        "liked" : GLOBAL_FILE_PATH + "",
                                                                },
                                                
                                        },


                                "in" :  {
                                                "user_profile" :        {
                                                                                "username_list" : GLOBAL_FILE_PATH + "",
                                                                                "user_id_list" : GLOBAL_FILE_PATH + "",
                                                                        },

                                                "tweet_timeline" :      {
                                                                                "user_id_list" : GLOBAL_FILE_PATH + "",
                                                                        },

                                                "user_follows" :        {
                                                                                "user_id_list" : GLOBAL_FILE_PATH + "",
                                                                        },

                                                "tweet_lookup" :        {
                                                                                "tweet_id_list" : GLOBAL_FILE_PATH + ""
                                                                        },
                                                "likes" :       {
                                                                        "user_id_list" : GLOBAL_FILE_PATH + "",
                                                                        "tweet_id_list" : GLOBAL_FILE_PATH + ""
                                                                },      
                                        }
                        }


        genopts =       {
                                "verbose?" : True
                        }

