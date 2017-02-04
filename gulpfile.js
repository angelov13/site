var gulp = require('gulp'),
concat = require('gulp-concat'),
uglify = require('gulp-uglify'),
sass = require('gulp-sass'),
cleanCSS = require('gulp-clean-css'),
autoprefixer = require('gulp-autoprefixer'),
browserSync = require('browser-sync').create('server');

gulp.task('server', function() {
    browserSync.init({
        proxy: "localhost:8000"
    });
});
gulp.task('post', function(){
	gulp.src('static/assets/desarrollo/sass/post.sass')
	.pipe(sass({outputStyle:'compressed'}))
	//.pipe(sass({outputStyle:'compact'}))
	//.pipe(sass({outputStyle:'expanded'}))
	.pipe(autoprefixer({
		cascade:false
	}))
	.pipe(concat('post.min.css'))
	.pipe(gulp.dest('static/assets/final/css/'))
	.pipe(browserSync.stream());
});

gulp.task('blog', function(){
	gulp.src('static/assets/desarrollo/sass/blog.sass')
	.pipe(sass({outputStyle:'compressed'}))
	//.pipe(sass({outputStyle:'compact'}))
	//.pipe(sass({outputStyle:'expanded'}))
	.pipe(autoprefixer({
		cascade:false
	}))
	.pipe(concat('blog.min.css'))
	.pipe(gulp.dest('static/assets/final/css/'))
	.pipe(browserSync.stream());
});

gulp.task('contacto', function(){
	gulp.src('static/assets/desarrollo/sass/contacto.sass')
	.pipe(sass({outputStyle:'compressed'}))
	//.pipe(sass({outputStyle:'compact'}))
	//.pipe(sass({outputStyle:'expanded'}))
	.pipe(autoprefixer({
		cascade:false
	}))
	.pipe(concat('contacto.min.css'))
	.pipe(gulp.dest('static/assets/final/css/'))
	.pipe(browserSync.stream());
});

gulp.task('servicios', function(){
	gulp.src('static/assets/desarrollo/sass/servicios.sass')
	.pipe(sass({outputStyle:'compressed'}))
	//.pipe(sass({outputStyle:'compact'}))
	//.pipe(sass({outputStyle:'expanded'}))
	.pipe(autoprefixer({
		cascade:false
	}))
	.pipe(concat('servicios.min.css'))
	.pipe(gulp.dest('static/assets/final/css/'))
	.pipe(browserSync.stream());
});

gulp.task('landing', function(){
	gulp.src('static/assets/desarrollo/sass/landing.sass')
	.pipe(sass({outputStyle:'compressed'}))
	//.pipe(sass({outputStyle:'compact'}))
	//.pipe(sass({outputStyle:'expanded'}))
	.pipe(autoprefixer({
		cascade:false
	}))
	.pipe(concat('landing.min.css'))
	.pipe(gulp.dest('static/assets/final/css/'))
	.pipe(browserSync.stream());
});

gulp.task('scripts', function(){
	gulp.src('static/assets/desarrollo/js/*.js')
	.pipe(uglify())
	.pipe(gulp.dest('static/assets/final/js/'));
});

gulp.task('analytics', function(){
	gulp.src('static/assets/desarrollo/js/analytics/*.js')
	.pipe(concat('analytics.js'))
	.pipe(gulp.dest('static/assets/final/js/'));
});

gulp.task('icon', function(){
	gulp.src('static/assets/final/fonts/style.css')
  .pipe(cleanCSS())
	.pipe(concat('icons.min.css'))
	.pipe(gulp.dest('static/assets/final/fonts/'))
	.pipe(browserSync.stream());
});

/*
*	Tarea por default
 */

gulp.task('default', ['server'],function(){

	gulp.watch('static/assets/desarrollo/js/*.js',['scripts']);
	gulp.watch('static/assets/desarrollo/js/analytics/*.js',['analytics']);
	gulp.watch("static/assets/final/js/*.js").on('change', browserSync.reload);
	gulp.watch('static/assets/desarrollo/sass/**/*.sass',['post','blog','contacto','servicios','landing']);
	gulp.watch('static/assets/final/fonts/style.css',['icon']);
	gulp.watch("templates/*.html").on('change', browserSync.reload);
});