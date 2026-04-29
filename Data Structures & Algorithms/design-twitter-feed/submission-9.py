class Twitter:

    def __init__(self):
        # BUCKET userid : list o tweets |

        # FOLLOWBUCKET userid : set following
        self.count = 0
        self.tweetBucket = {}
        self.followBucket = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        val = (self.count, tweetId)
        self.count -= 1
        if self.tweetBucket.get(userId):
            self.tweetBucket[userId].append(val)
            return

        
        self.tweetBucket[userId] = [val]
        self.follow(userId, userId)

        
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []

        # ASSUMPTION is userID exists?

        for posterId in self.followBucket.get(userId):
            posts.extend(self.tweetBucket.get(posterId))

        import heapq
        
        heapq.heapify(posts)
        print(posts)
        tenLargest = heapq.nsmallest(10, posts)
        
        tweets = [val[1] for val in tenLargest]

        return tweets



    def follow(self, followerId: int, followeeId: int) -> None:
        followers = self.followBucket.get(followerId)
        if followers:
            followers.add(followeeId)
            return
        
        self.followBucket[followerId] = {followeeId}
        
            
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        followers = self.followBucket.get(followerId)
        if followers:
            followers.discard(followeeId)
            return
        
