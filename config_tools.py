

class ctools:

        """configuration tools"""


        authorization = {
                                
                                "bearer_token" : "AAAAAAAAAAAAAAAAAAAAAB0ThAEAAAAAXyFc9qroqhUxhIk3advvnkqgSPw%3DXTCuvsSRPXoi3oL5hA2p0rQKWwn8Qlrpcm7m91X9lVDmoAZ0D8",
                                # api key = 8zliFVcnnPVmBGngiDtgZeD5U
                                "api_key" : "8zliFVcnnPVmBGngiDtgZeD5U",
                                # api secret key = qx7hbX4OVirqEP4S3RXSTnUv3hZLKVYrzTuezExu9Hcd3s3q0R
                                "api_secret_key" : "qx7hbX4OVirqEP4S3RXSTnUv3hZLKVYrzTuezExu9Hcd3s3q0R"
                        }

        tweet_lookup_params =   {
                                        "read_from_file?" : True,

                                        "tweet_ids" : "1582582264185049088,1582582042063093760,1582547658039623680",

                                        "request_params" :      {
                                                                       "expansions" : None,#"attachments.poll_ids,attachments.media_keys,author_id,edit_history_tweet_ids,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id",
                                                                        "media.fields" : None,#"duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics,non_public_metrics,organic_metrics,promoted_metrics,alt_text,variants",
                                                                        "place.fields" : None,#"contained_within,country,country_code,full_name,geo,id,name,place_type",
                                                                        "poll.fields" : None,#"duration_minutes,end_datetime,id,options,voting_status",
                                                                        "tweet.fields" : None,#"attachments,author_id,context_annotations,conversation_id,created_at,edit_controls,entities,geo,id,in_reply_to_user_id,lang,public_metrics,possibly_sensitive,referenced_tweets,reply_settings,source,text,withheld", 
                                                                }
                                }

        tweet_timeline_params = {

                                        "read_from_file?" : False,

                                        "user_id" : "44196397",

                                        "pagination" :  {
                                                                "paginate?" : False,
                                                                "page_count" : 2
                                                        },

                                        "request_params" :      {    
                                                                        "expansions" : "attachments.poll_ids,attachments.media_keys,author_id,edit_history_tweet_ids,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id",
                                                                        "max_results" : "5",
                                                                        "media.fields" : None,#"duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics,non_public_metrics,organic_metrics,promoted_metrics,alt_text,variants",
                                                                        "place.fields" : None,#"contained_within,country,country_code,full_name,geo,id,name,place_type",
                                                                        "poll.fields" : None,#"duration_minutes,end_datetime,id,options,voting_status",
                                                                        "tweet.fields" : None,#"attachments,author_id,context_annotations,conversation_id,created_at,edit_controls,entities,geo,id,in_reply_to_user_id,lang,public_metrics,possibly_sensitive,referenced_tweets,reply_settings,source,text,withheld",
                                                                        "pagination_token" : None,
                                                                        "exclude" : None,
                                                                        "start_time" : None,
                                                                        "end_time" : None,
                                                                        "until_id" : None,
                                                                },
                                }       


        user_profile_params =   {       
                                        "usernames" : "elonmusk",

                                        "user_id" : None,#"44196397",

                                        "search_by_username?": True,

                                        "request_params" :      {
                                                                        "user.fields" : None,#"description,id,public_metrics,created_at,entities,location,name,profile_image_url,protected,url,username,verified,withheld",
                                                                        "expansions" : None,#"pinned_tweet_id",
                                                                        "max_results" : None,
                                                                },

                                        "read_from_file?" : False,               
                                }


        user_follows_params =   {
                                        "read_from_file?" : False,

                                        "user_id" : "44196397",

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
                                "read_from_file?": True,

                                "tweet_id" : "1582547658039623680",

                                "user_id" : "822215679726100480",

                                "pagination" :  {
                                                        "paginate?" : True,
                                                        "page_count" : 2,
                                                },

                                "liking_request_params" :       {
                                                                        "user.fields" : "description,id,public_metrics,created_at,entities,location,name,profile_image_url,protected,url,username,verified,withheld",
                                                                        "expansions" : "pinned_tweet_id",
                                                                        "max_results" : "5",
                                                                        "pagination_token" : None
                                                                },

                                "liked_request_params" :        {    
                                                                        "expansions" : None,#"attachments.poll_ids,attachments.media_keys,author_id,edit_history_tweet_ids,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id",
                                                                        "max_results" : "5",
                                                                        "media.fields" : None,#"duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics,non_public_metrics,organic_metrics,promoted_metrics,alt_text,variants",
                                                                        "place.fields" : None,#"contained_within,country,country_code,full_name,geo,id,name,place_type",
                                                                        "poll.fields" : None,#"duration_minutes,end_datetime,id,options,voting_status",
                                                                        "tweet.fields" : None,#"attachments,author_id,context_annotations,conversation_id,created_at,edit_controls,entities,geo,id,in_reply_to_user_id,lang,public_metrics,possibly_sensitive,referenced_tweets,reply_settings,source,text,withheld",
                                                                        "pagination_token" : None,
                                                                        "exclude" : None,
                                                                        "start_time" : None,
                                                                        "end_time" : None,
                                                                        "until_id" : None,
                                                                },
                        }

        GLOBAL_FILE_PATH = "/home/kinder/Documents/python/tweet/io/"

        file_IO =       {
                                "out" : {
                                                "testfile" : "elondump.txt",

                                                "user_profile" :        {
                                                                                "user_profiles" : GLOBAL_FILE_PATH + "user_profiles.txt",
                                                                        },

                                                "tweet_timeline" :      {
                                                                                "tweet_timelines" : GLOBAL_FILE_PATH + "timeline.txt",
                                                                        },

                                                "user_follows" :        {
                                                                                "user_followers" : GLOBAL_FILE_PATH + "followers.txt",

                                                                                "user_following" : GLOBAL_FILE_PATH + "following.txt"
                                                                        },

                                                "tweet_lookup" :        {
                                                                                "tweets" : GLOBAL_FILE_PATH + "tweets.txt"
                                                                        },

                                                "likes" :       {
                                                                        "liking" : GLOBAL_FILE_PATH + "likes.txt",
                                                                        "liked" : GLOBAL_FILE_PATH + "likes.txt",
                                                                },

                                                "testfile" : GLOBAL_FILE_PATH + "testfile.txt"
                                                
                                        },

                                "in" :  {
                                                "user_profile" :        {
                                                                                "username_list" : GLOBAL_FILE_PATH + "usernamelist.txt",
                                                                                "user_id_list" : GLOBAL_FILE_PATH + "user_id_list.txt",
                                                                        },

                                                "tweet_timeline" :      {
                                                                                "user_id_list" : GLOBAL_FILE_PATH + "user_id_list.txt",
                                                                        },

                                                "user_follows" :        {
                                                                                "user_id_list" : GLOBAL_FILE_PATH + "user_id_list.txt",
                                                                        },

                                                "tweet_lookup" :        {
                                                                                "tweet_id_list" : GLOBAL_FILE_PATH + "tweet_id_list.txt"
                                                                        },
                                                "likes" :       {
                                                                        "user_id_list" : GLOBAL_FILE_PATH + "user_id_list.txt",
                                                                        "tweet_id_list" : GLOBAL_FILE_PATH + "tweet_id_list.txt"
                                                                },      
                                                                        
                                                "testfile" : GLOBAL_FILE_PATH + "raw_list.txt",
                                        }
                        }


        genopts =       {
                                "verbose?" : True
                        }

