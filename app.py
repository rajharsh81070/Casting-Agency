import os
import json
from flask import Flask, request, abort, jsonify
#from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actors, Movies
from auth import AuthError, requires_auth


RECS_PER_PAGE = 12


def create_app(test_config=None):
    # create and configure the app

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    '''
    CORS Headers
    '''

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    '''
    To Keep a common pagination method to be called
    by different endpoints
    '''

    def paginate_questions(request, selection):
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * RECS_PER_PAGE
        end = start + RECS_PER_PAGE

        recs_format = [record.format() for record in selection]
        page_recs = recs_format[start:end]
        return page_recs

    '''
    Sample Endpoint: To test if the app is up and running
    '''

    @app.route('/', methods=['GET'])
    def get_init():
        return jsonify({
            'success': True,
            'SampleTest': 'Hello World'
        })

    '''
    Implemented endpoint GET /actors
        - it will GET all actors with their description
        - it will require the 'get:actors' permission
        - returns status code 200 and json {"success": True,
            "actors": actors} where actors is the list of actors
            or appropriate status code indicating reason for failure
    '''

    @app.route('/actors', methods=['GET'])
    @requires_auth(permission='get:actors')
    def get_actors(payload):
        try:
            selections = Actors.query.order_by(Actors.id).all()
            paged_actors = paginate_questions(request, selections)
            total_actors = len(selections)
            return jsonify({
                'success': True,
                'actors': paged_actors,
                'total-actors': total_actors
            })
        except Exception:
            abort(422)

    '''
    Implemented endpoint POST /actors
        - it will create a new row in the Actors table
        - it will require the 'post:actors' permission
        - returns status code 200 and json {"success": True,
            "actors": actor} where actor is an array containing only 
            the newly created actor
            or appropriate status code indicating reason for failure
    '''

    @app.route('/actors', methods=['POST'])
    @requires_auth(permission='post:actors')
    def post_actors(payload):
        add_actor = request.get_json()
        actor_name = add_actor.get('name')
        actor_gender = add_actor.get('gender')
        actor_age = add_actor.get('age')

        if actor_name is None:
            abort(422)

        if actor_gender is None:
            abort(422)

        if actor_age is None:
            abort(422)

        try:
            new_actor = Actors(name=actor_name,
                               gender=actor_gender,
                               age=actor_age)
            new_actor.insert()

            return jsonify({
                "success": True,
                "actor-added": new_actor.id
            })

        except Exception:
            abort(422)

    '''
    Implemented endpoint PATCH /actors/<id>
        - where <id> is the existing actors id
        - it will respond with a 404 error if <id> is not found
        - it will update the corresponding row for <id>
        - it will require the 'patch:actors' permission
        - returns status code 200 and json {"success": True,
            "actors": actor} where actors is an array containing only
            the updated actor or appropriate status code indicating
            reason for failure
    '''

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth(permission='patch:actors')
    def patch_actors(payload, id):
        actor = Actors.query.filter(Actors.id == id).first()
        if not actor:
            abort(404)

        update_actor_req = request.get_json()

        if update_actor_req is None:
            abort(422)

        try:
            if 'name' in update_actor_req:
                actor.name = update_actor_req['name']

            if 'gender' in update_actor_req:
                actor.gender = update_actor_req['gender']

            if 'age' in update_actor_req:
                actor.age = update_actor_req['age']

            actor.update()

            return jsonify({
                "success": True,
                "actor-updated": actor.id
            })

        except Exception:
            abort(422)

    '''
    Implemented endpoint DELETE /actors/<id>
        - where <id> is the existing actors id
        - it will respond with a 404 error if <id> is not found
        - it will delete the corresponding row for <id>
        - it will require the 'delete:actors' permission
        - returns status code 200 and json {"success": True,
            "delete": id} where id is the id of the deleted record
            or appropriate status code indicating reason for failure
    '''

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth(permission='delete:actors')
    def delete_actors(payload, id):
        actor = Actors.query.filter(Actors.id == id).first()
        if not actor:
            abort(404)
        try:
            actor.delete()
            return jsonify({
                "success": True,
                "actor-deleted": actor.id
            })

        except Exception:
            abort(422)

    '''
    Implemented endpoint GET /movies
        - it will GET all movies with their release date
        - it will require the 'get:movies' permission
        - returns status code 200 and json {"success": True,
            "movies": movies} where movies is the list of movies
            or appropriate status code indicating reason for failure
    '''

    @app.route('/movies', methods=['GET'])
    @requires_auth(permission='get:movies')
    def get_movies(payload):
        try:
            selections = Movies.query.order_by(Movies.id).all()
            paged_movies = paginate_questions(request, selections)
            total_movies = len(selections)
            return jsonify({
                'success': True,
                'movies': paged_movies,
                'total-movies': total_movies
            })
        except Exception:
            abort(422)

    '''
    Implemented endpoint POST /movies
        - it will create a new row in the Movies table
        - it will require the 'post:movies' permission
        - returns status code 200 and json {"success": True,
            "movies": movies} where movie is an array containing only 
            the newly created movie
            or appropriate status code indicating reason for failure
    '''

    @app.route('/movies', methods=['POST'])
    @requires_auth(permission='post:movies')
    def post_movies(payload):
        add_movie = request.get_json()
        movie_title = add_movie.get('title')
        movie_rls_date = add_movie.get('release_date')

        if movie_title is None:
            abort(422)

        if movie_rls_date is None:
            abort(422)

        try:
            new_movie = Movies(title=movie_title,
                               release_date=movie_rls_date)
            new_movie.insert()

            return jsonify({
                "success": True,
                "movie-added": new_movie.id
            })

        except Exception:
            abort(422)

    '''
    Implemented endpoint PATCH /movies/<id>
        - where <id> is the existing movies id
        - it will respond with a 404 error if <id> is not found
        - it will update the corresponding row for <id>
        - it will require the 'patch:movies' permission
        - returns status code 200 and json {"success": True,
            "movies": movies} where actors is an array containing only
            the updated actor or appropriate status code indicating
            reason for failure
    '''

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth(permission='patch:movies')
    def patch_movies(payload, id):
        movie = Movies.query.filter(Movies.id == id).first()

        if not movie:
            abort(404)

        update_movie_req = request.get_json()

        if update_movie_req is None:
            abort(422)

        try:
            if 'title' in update_movie_req:
                movie.title = update_movie_req['title']

            if 'release_date' in update_movie_req:
                movie.release_date = update_movie_req['release_date']

            movie.update()

            return jsonify({
                "success": True,
                "movie-updated": movie.id
            })

        except Exception:
            abort(422)

    '''
    Implemented endpoint DELETE /movies/<id>
        - where <id> is the existing movies id
        - it will respond with a 404 error if <id> is not found
        - it will delete the corresponding row for <id>
        - it will require the 'delete:movies' permission
        - returns status code 200 and json {"success": True,
            "delete": id} where id is the id of the deleted record
            or appropriate status code indicating reason for failure
    '''

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth(permission='delete:movies')
    def delete_movies(payload, id):
        movie = Movies.query.filter(Movies.id == id).first()

        if not movie:
            abort(404)
        try:
            movie.delete()
            return jsonify({
                "success": True,
                "movie-deleted": movie.id
            })

        except Exception:
            abort(422)

    '''
    Error handlers for possible errors including 400, 401, 403,
    404, 405, 422 and 500.
    '''

    @app.errorhandler(400)
    def badRequest(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized"
        }), 401

    @app.errorhandler(403)
    def accessForbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "Access Denied/Forbidden"
        }), 403

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
        }), 404

    @app.errorhandler(405)
    def notAllowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method not Allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(500)
    def serverError(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    @app.errorhandler(AuthError)
    def auth_error(e):
        return jsonify({
            "success": False,
            "error": e.status_code,
            "message": e.error
        }), e.status_code

    return app


app = create_app()

if __name__ == '__main__':
    #    app.run(host='0.0.0.0', port=8080, debug=True)
    app.run(host='0.0.0.0', port=8080, debug=True)
