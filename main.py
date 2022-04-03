from users import reddit
import api.bearer_api as ba
import api.place_api as pa

# start cordinates
x = 284
y = 344
class bot:
    def target(self, uname, passwd, i):
        try:
            BearerAPI = ba.Bearer()
            PlaceAPI = pa.Place()
            api_token = BearerAPI.fetch_token(uname, passwd)
            result = PlaceAPI.place_tile(x+i, y, 6, api_token)
            print(result)
        except:
            pass

def main():
    # start and end of range of pixels to be changed
    start = 0
    for i in reddit:
        t = bot()
        t.target(i, reddit.get(i), start)
        start += 1
        del t

if __name__ == '__main__':
    main()