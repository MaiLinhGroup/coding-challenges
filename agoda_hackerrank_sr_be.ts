/**
* There's always at least one meeting that needs to be scheduled,
* but the list of meetings is unordered.
* Additionally, one can safely assume that a new meeting can start
* in the same room as the previous one when the previous one ends
* at the same time as the new one would've started.
*/
function getMinNumMeetingRooms(meetings: number[][]):number{
    let minNumOfMeetingRooms = 1;
    const activeMeetingsEndtime: number[] = [];

    if(meetings.length === 1) {
        return minNumOfMeetingRooms;
    }
    meetings.sort((a,b) => a[0] - b[0]);
    console.log(`Meetings after sorting by their starting time, starting with the earliest one: ${JSON.stringify(meetings)}`);

    meetings.forEach((meeting) => {
        const [start, end] = [meeting[0], meeting[1]];
        if(activeMeetingsEndtime[0] === undefined){
            activeMeetingsEndtime.push(end);
            return
        }
        if(start >= activeMeetingsEndtime[0]){
            activeMeetingsEndtime.shift();
        }else{
            minNumOfMeetingRooms++;
        }
        activeMeetingsEndtime.push(end);
        activeMeetingsEndtime.sort((a,b) => a-b);
    });

    return minNumOfMeetingRooms;
}

const meetings = [
    [1,4],
    [7,10],
    [5,6],
    [5,9],
    [1,5],
];
console.log(`Given this list of meetings: ${JSON.stringify(meetings)} with their respective start and end time that need to be scheduled for today`);
console.log(`The minimum number of booked rooms that is required to scheduled them all is ${getMinNumMeetingRooms(meetings)}`);
