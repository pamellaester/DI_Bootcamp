class video {
    constructor(title, uploader, time) {
                this.title = title;
                this.uploader = uploader;
                this.time = time;
        
            }

watch() {
    return `${this.uploader} watched all ${this.time} of ${this.title}!`
}

}

const a = new video("Video 1", "User1", 180);
console.log(a.watch())
const b = new video("Video 2", "User2", 420);
console.log(b.watch())