export AUTH0_DOMAIN='fsnd-harsh-capstone.us.auth0.com'
export ALGORITHMS='RS256'
export API_AUDIENCE='cagency'

#local database url
export DATABASE_URL='postgres://postgres:12345678@localhost:5432/castagency'

#heroku database url
export DATABASE_URL='postgres://hkyeustnkszunx:522a8ad98d5a8a8d9a6cc22ba930469e35f6b714757e032dc754009dc31bccf9@ec2-3-216-129-140.compute-1.amazonaws.com:5432/de37vpaq4ak84t'

#JWTS for all the 3 roles/users: Latest with 24 hours expiration
export ASSISTANT_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllBbHRoWTBYWTA1T21BWms1VnAxWSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtaGFyc2gtY2Fwc3RvbmUudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMzE4NDg0ZDUzMDdhMDAzZDI5MzE4YiIsImF1ZCI6ImNhZ2VuY3kiLCJpYXQiOjE1OTcxMzU4MzksImV4cCI6MTU5NzE0MzAzOSwiYXpwIjoiYU9sQWxUSW9MaGlHbUZOVGZ3UTI1anpkSlI3dUJrN2siLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.SXzYIE3dascoxs2d4ziR2LaeLTkSAHhnMI9PsbLYVqY4VcQ3zaduooTTLvTGnnQ22LLJ0mP_fj7mr39c3IakPkwaiAjYdT0t04yXR-XezihdNoeLpeYv0E-9opDFs3t0ZigZ2qRWXJJ55p0Zu7WcaF_4aBzn2KL3dzCRgmt-R9Z2T3L8S1hK7xPN82dy6Pu9r8Fl0fMHXqRmqjnvKBYQVbfOpfrrd3hjT4kPh5KVAginpYNFBQ4E7E3ly2rVljISkbMAbqxxlvadftISKVCN2_Qp0cXxGonqboCTLXSoythH1BNq0UdgnZq3-z46kZkoYeWh_aqj0dL2idivYwdLiA'
export DIRECTOR_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllBbHRoWTBYWTA1T21BWms1VnAxWSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtaGFyc2gtY2Fwc3RvbmUudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMzE4NDg0ZDUzMDdhMDAzZDI5MzE4YiIsImF1ZCI6ImNhZ2VuY3kiLCJpYXQiOjE1OTcxMzY0NTQsImV4cCI6MTU5NzE0MzY1NCwiYXpwIjoiYU9sQWxUSW9MaGlHbUZOVGZ3UTI1anpkSlI3dUJrN2siLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.PZRUdsp6qJqjw7AD_o_mF3vDnhSZoJyE0X5zi-L3QtmQ6b2bwguncddsLEI65D395ztmG-DaBLGXhytHPDqRsVTcCkzsLDqVFFVTstd5f-pV6lDQkN8-V7wmB_AdDc3wqluE173xPpTss3morRN2lXpuuNAqW1A9r2tTe8Mf6eqkMShgeF_sg_lNjq4GtEnHz31Yv3wfdu5U210N8XsB48_9fsnkpl4ESqPVsdYfOSLgmkG1spBKOT4EdaUi3ObBHL5wFGRw8UwATGhl0J9mWOjmyX82a9DpVBfic1F59KOKe8vndCmXED8RZbaxtNpov1g3oeP2CIAEtqxHWVLrRg'
export PRODUCER_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllBbHRoWTBYWTA1T21BWms1VnAxWSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtaGFyc2gtY2Fwc3RvbmUudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMzE4NDg0ZDUzMDdhMDAzZDI5MzE4YiIsImF1ZCI6ImNhZ2VuY3kiLCJpYXQiOjE1OTcxMzY1OTksImV4cCI6MTU5NzE0Mzc5OSwiYXpwIjoiYU9sQWxUSW9MaGlHbUZOVGZ3UTI1anpkSlI3dUJrN2siLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.anZqmO_LekUKgcYiMRTGuvPZlhLc0f5et-lW8K4yEGIwna3ORWQoUFurwOssRni3wJGHgEHVak83lxxeGhiO07iabVsbzOMCTb9WwuvJWggJePbzEmmUG40lh1eRE1dVYf6PfXtkZcPOxsJCtrSDucjrU_FZsOqV19A8hdX_1dDXGoOEq4ROiKlYQijBzAGbDWovXrX4dEzEuYOWQC5Bnzj6HWv5J4aQiIayPN7z7ifyxlRTeeF4u0W1XhZwgna0Kaf0rGTinYFPajArhnJ9PIkOykz6-UCdjsFRZD5rrmrA-viXDrzhDwHQ7gYmo8L7bN7zp9Dh4n_DwOkTYDV53g'
