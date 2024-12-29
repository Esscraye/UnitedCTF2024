
const code = "const fs = require('fs'); console.log(fs.readFileSync('flag.txt'));";
const CODE = "CONST FS = REQUIRE('FS'); CONSOLE.LOG(FS.READFILESYNC('FLAG.TXT'));";
// eval(CODE);

eval(code);
// async function challenge() {
//   console.log(challenge.toString());
//   try {
//     const linereader = require("readline").createInterface({
//       input: process.stdin,
//     });

//     process.stdout.write("> ");
//     for await (const line of linereader) {
//       if (/[0-9a-z]/i.test(line)) throw new Error("ILLEGAL INPUT DETECTED!");
//       eval(line);
//       process.stdout.write("> ");
//     }
//   } catch (err) {
//     console.log(err.message);
//   }
// }
// challenge();




